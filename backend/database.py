import pymysql
import inspect


def database_connect():
    return pymysql.connect(
        host="rm-cn-g6z3tw7xl00052co.rwlb.rds.aliyuncs.com",
        port=3306,
        user="buaa_python_2024",
        passwd="DCJBzxhy2024",
        db="python_todo",
        charset="utf8mb4",
        binary_prefix=True,
    )


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
        print(f"{inspect.stack()[1].function} error!")
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
        print(f"{inspect.stack()[1].function} error!")
        print(e)
        return False


def get_constant_info(file_name, constant_name):
    cmd = """
    SELECT constant_value
    FROM constants
    WHERE  constant_name = %s AND file_name = %s
    """
    args = (constant_name, file_name)
    return database_read(cmd, args)


def delete(table_name, identifier_name, identifier):
    cmd = f"""
    DELETE FROM {table_name}
    WHERE {identifier_name} = %s
    """
    args = (identifier,)
    return database_write(cmd, args)


def reset_info(subject_name, identifier_name, identifier, info_category, info):
    cmd = f"""
    UPDATE {subject_name}s
    SET {subject_name}_{info_category} = %s
    WHERE {identifier_name} = %s
    """
    args = (info, identifier)
    return database_write(cmd, args)


def get_info(subject_name, identifier_name, identifier, info_category):
    cmd = f"""
    SELECT {subject_name}_{info_category}
    FROM {subject_name}s
    WHERE {identifier_name} = %s
    """
    args = (identifier,)
    return database_read(cmd, args)


def get(table_name, identifier_name, identifier):
    cmd = f"""
    SELECT * FROM {table_name}
    WHERE {identifier_name} = %s
    """
    args = (identifier,)
    return database_read(cmd, args, False)


def join(
    table_name,
    reference_table_name,
    identifier_name,
    identifier,
    condition_cmd,
    condition_args,
):
    cmd = (
        f"""
    SELECT t.*
    FROM {table_name} t
    JOIN {reference_table_name} u ON t.{identifier_name} = u.{identifier_name}
    WHERE u.{identifier_name} = %s
    """
        + condition_cmd
    )
    args = (identifier,) + condition_args
    return database_read(cmd, args, False)


def list_all(table_name):
    cmd = f"""
    SELECT * FROM {table_name}
    """
    return (get_list_head(table_name),) + database_read(cmd, (), False)


def list_info(table_name, identifier_name, identifier):
    return get_list_head(table_name), get(table_name, identifier_name, identifier)


def get_list_head(table_name):
    return tuple(
        [results[0] for results in database_read("DESCRIBE " + table_name, (), False)]
    )


def print_list(lis):
    for item in lis:
        print(item)
