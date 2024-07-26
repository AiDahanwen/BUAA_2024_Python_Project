import bcrypt
from backend.database import *
from datetime import date
from backend.database import *
import oss2

# 填写RAM用户的访问密钥（AccessKey ID和AccessKey Secret）
accessKeyId = "LTAI5tNicQ2EWpzvo7YAYB7D"
accessKeySecret = "UvT8HCUfLb8Y8Vu2hPgSADdZyNmQCV"
# 使用代码嵌入的RAM用户的访问密钥配置访问凭证
auth = oss2.Auth(accessKeyId, accessKeySecret)
# 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
endpoint = "https://oss-cn-beijing.aliyuncs.com"

# 填写Bucket名称
bucket = oss2.Bucket(auth, endpoint, "foolish-han")


def gen_hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return salt, hashed_password


def get_hash_password(password, salt):
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def reset_user_password(user_email, user_password):
    salt, user_password_hash = gen_hash_password(user_password)
    return reset_user_info(
        user_email, "password_hash", user_password_hash
    ) and reset_user_info(user_email, "hash_salt", salt)


def is_user_password_correct(user_email, user_password):
    user_hash_salt = get_user_info(user_email, "hash_salt")
    user_password_hash = get_user_info(user_email, "password_hash")
    if user_hash_salt and user_password_hash:
        return user_password_hash == get_hash_password(user_password, user_hash_salt)
    return False


def add_user(user_name, user_email, user_password):
    cmd = """
    INSERT INTO users (user_name, user_email, user_password_hash, user_hash_salt, user_register_date)
    VALUES(%s, %s, %s, %s, %s)
    """
    salt, user_password_hash = gen_hash_password(user_password)
    args = (user_name, user_email, user_password_hash, salt, date.today())
    return database_write(cmd, args)


def delete_user(user_email):
    return delete("users", "user_email", user_email)


def reset_user_info(user_email, info_category, user_info):
    # info_category: name, avatar_url, signature
    return reset_info("user", "user_email", user_email, info_category, user_info)


def get_user_info(user_email, info_category):
    # info_category: name, avatar_url, signature
    return get_info("user", "user_email", user_email, info_category)


def is_user_email_exist(user_email):
    cmd = """
    SELECT EXISTS(
    SELECT 1 FROM users WHERE user_email = %s
    ) AS user_email_exists;
    """
    args = (user_email,)
    return database_read(cmd, args)


def list_all_users():
    return list_all("users")


def list_user_info(user_email):
    return list_info("users", "user_email", user_email)


def modify_user_avatar(user_email, avatar_url):
    avatar_name = avatar_url.split("/")[-1]
    temp = str(user_email) + "/" + "user_avatar/" + avatar_name
    bucket.put_object_from_file(temp, avatar_url)
    avatar_url = "https://foolish-han.oss-cn-beijing.aliyuncs.com/" + temp
    reset_user_info(user_email, "avatar_url", avatar_url)


def store_local_user_email_password(user_email, user_password):
    with open("local/storage.txt", "w") as fd:
        fd.write(f"{user_email} {user_password}")


def get_local_user_email_password():
    try:
        with open("local/storage.txt", "r") as fd:
            data = fd.read()
        return data.split()
    except FileNotFoundError:
        return False
