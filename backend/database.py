import pymysql
import bcrypt


def database_connect():
    return pymysql.connect(host='rm-cn-g6z3tw7xl00052co.rwlb.rds.aliyuncs.com',
                           port=3306,
                           user='buaa_python_2024',
                           passwd='DCJBzxhy2024',
                           db='python_todo',
                           charset='utf8mb4',
                           binary_prefix=True)


def database_read(cmd, args, fetchone=True):
    try:
        connection = database_connect()
        cursor = connection.cursor()
        cursor.execute(cmd, args)
        if fetchone:
            result = cursor.fetchone()[0]
        else:
            result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Exception as e:
        return False


def database_write(cmd, args):
    try:
        connection = database_connect()
        cursor = connection.cursor()
        cursor.execute(cmd, args)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        return False


def gen_hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return salt, hashed_password


def get_hash_password(password, salt):
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def get_constant(file_name, constant_name):
    cmd = """
        SELECT constant_value
        FROM constants
        WHERE  constant_name = %s AND file_name = %s"""
    args = (constant_name, file_name)
    return database_read(cmd, args)


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


def reset_name(user_email, user_name):
    cmd = """
        UPDATE users
        SET user_name = %s
        WHERE user_email = %s
        """
    args = (user_name, user_email)
    return database_write(cmd, args)


def reset_signature(user_email, user_signature):
    cmd = """
    UPDATE users
    SET signature = %s
    WHERE user_email = %s
    """
    args = (user_signature, user_email)
    return database_write(cmd, args)


def delete_user(user_email):
    cmd = """
    DELETE FROM users
    WHERE user_email = %s
    """
    args = (user_email,)
    return database_write(cmd, args)


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


def list_users():
    cmd = """
    SELECT * FROM users
    """
    return (get_list_head(),) + database_read(cmd, (), False)


def list_user_info(user_email):
    cmd = """
    SELECT  * FROM users
    WHERE user_email = %s
    """
    args = user_email
    return get_list_head(), database_read(cmd, args)


def get_list_head():
    return tuple([results[0] for results in database_read('DESCRIBE users', (), False)])
