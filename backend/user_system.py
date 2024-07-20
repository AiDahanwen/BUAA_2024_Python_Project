import bcrypt
from database import *


def gen_hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return salt, hashed_password


def get_hash_password(password, salt):
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def reset_user_password(user_email, user_password):
    salt, user_password_hash = gen_hash_password(user_password)
    return (reset_user_info(user_email, "password_hash", user_password_hash)
            and reset_user_info(user_email, "hash_salt", salt))


def is_user_password_correct(user_email, user_password):
    user_hash_salt = get_user_info(user_email, "hash_salt")
    user_password_hash = get_user_info(user_email, "password_hash")
    if user_hash_salt and user_password_hash:
        return user_password_hash == get_hash_password(user_password, user_hash_salt)
    return False


def add_user(user_name, user_email, user_password):
    cmd = """
    INSERT INTO users (user_name, user_email, user_password_hash, user_hash_salt)
    VALUES(%s, %s, %s, %s)
    """
    salt, user_password_hash = gen_hash_password(user_password)
    args = (user_name, user_email, user_password_hash, salt)
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


# print(delete_user('2895227477@qq.com'))
# print(add_user('wt', '2895227477@qq.com', '12345678'))
print(reset_user_info('2895227477@qq.com', ''))
