import pymysql
import inspect


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
        print(f'{inspect.stack()[1].function} error!')
        print(e)
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
        print(f'{inspect.stack()[1].function} error!')
        print(e)
        return False


def get_constant(file_name, constant_name):
    cmd = """
    SELECT constant_value
    FROM constants
    WHERE  constant_name = %s AND file_name = %s
    """
    args = (constant_name, file_name)
    return database_read(cmd, args)


def delete(table_name, identifier_name, identifier):
    cmd = """
    DELETE FROM """ + table_name + """
    WHERE """ + identifier_name + """ = %s
    """
    args = (identifier,)
    return database_write(cmd, args)


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


def get_list_head(list_name):
    return tuple([results[0] for results in database_read('DESCRIBE ' + list_name, (), False)])
