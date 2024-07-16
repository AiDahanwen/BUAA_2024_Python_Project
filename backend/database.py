import pymysql


def get_constant(file_name, constant_name):
    connection = pymysql.connect(host='rm-cn-g6z3tw7xl00052co.rwlb.rds.aliyuncs.com',
                                 port=3306,
                                 user='buaa_python_2024',
                                 passwd='DCJBzxhy2024',
                                 db='python_todo')
    cursor = connection.cursor()
    query = "SELECT constant_value FROM constants WHERE  constant_name = %s AND file_name = %s"
    cursor.execute(query, (constant_name, file_name))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] if result else None
