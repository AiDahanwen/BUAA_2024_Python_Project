import bcrypt
from database import *


def gen_hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return salt, hashed_password


def get_hash_password(password, salt):
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def add_user(user_name, user_email, user_password):
    cmd = """
    INSERT INTO users (user_name, user_email, user_password_hash, hash_salt)
    VALUES(%s, %s, %s, %s)
    """
    salt, user_password_hash = gen_hash_password(user_password)
    args = (user_name, user_email, user_password_hash, salt)
    return database_write(cmd, args)


def reset_password(user_email, user_password):
    salt, user_password_hash = gen_hash_password(user_password)
    cmd = """
    UPDATE users
    SET user_password_hash = %s, hash_salt = %s
    WHERE user_email = %s
    """
    args = (user_password_hash, salt, user_email)
    return database_write(cmd, args)


def reset_user_info(user_email, info_category, user_info):
    # info_category: name, avatar_url, signature
    cmd = """
    UPDATE users
    SET user_""" + info_category + """ = %s
    WHERE user_email = %s
    """
    args = (user_info, user_email)
    return database_write(cmd, args)


def delete_user(user_email):
    return delete("users", "user_email", user_email)


def is_user_password_correct(user_email, user_password):
    cmd = """
    SELECT hash_salt
    FROM users
    WHERE user_email = %s
    """
    args = (user_email,)
    salt = database_read(cmd, args)
    if not salt:
        return False
    user_password_hash = get_hash_password(user_password, salt)
    cmd = """
    SELECT user_password_hash
    FROM users
    WHERE user_email = %s
    """
    args = (user_email,)
    result = database_read(cmd, args)
    if result:
        return user_password_hash == result
    return False


def is_user_email_exist(user_email):
    cmd = """
    SELECT COUNT(*) FROM users WHERE user_email = %s
    """
    args = (user_email,)
    result = database_read(cmd, args)
    return result > 0


def get_user_info(user_email, info_category):
    # info_category: name, avatar_url, signature
    cmd = """
    SELECT user_""" + info_category + """
    FROM users
    WHERE user_email = %s
    """
    args = (user_email,)
    return database_read(cmd, args)


def list_users():
    cmd = """
    SELECT * FROM users
    """
    return (get_list_head("users"),) + database_read(cmd, (), False)


def list_user_info(user_email):
    cmd = """
    SELECT * FROM users
    WHERE user_email = %s
    """
    args = user_email
    return get_list_head("users"), database_read(cmd, args)
