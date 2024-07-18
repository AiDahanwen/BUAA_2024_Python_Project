import datetime
from database import *


class TaskStatus(str):
    PENDING = 'pending'
    UNDERWAY = 'underway'
    COMPLETED = 'completed'
    EXPIRED = 'expired'


class Task():
    
    def __init__(self, status=TaskStatus.PENDING, is_vital=False, title='', content='',
                 start_time=None, end_time=None, deadline=None):
        self.status = status
        self.is_vital = is_vital
        self.title = title
        self.content = content
        self.start_time = start_time
        self.end_time = end_time
        self.deadline = deadline


def add_task(user_email, task_is_vital, task_title, task_content, task_deadline):
    cmd = """
    INSERT INTO tasks (user_email, task_is_vital, task_title, task_content, task_create_time, task_deadline)
    VALUE (%s, %s, %s ,%s, %s, %s)
    """
    task_create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    args = (user_email, task_is_vital, task_title, task_content, task_create_time, task_deadline)
    return database_write(cmd, args)


def delete_task(task_id):
    cmd = """
        DELETE FROM tasks
        WHERE task_id = %s
        """
    args = (task_id,)
    return database_write(cmd, args)


def reset_task_info(task_id, info_category, task_info):
    # info_category: status, is_vital, title, content, create_time, deadline, complete_time
    cmd = """
    UPDATE tasks
    SET task_""" + info_category + """ = %s
    WHERE task_id = %s
    """
    args = (task_info, task_id)
    return database_write(cmd, args)


def get_task_info(task_id, info_category):
    # info_category: status, is_vital, title, content, create_time, deadline, complete_time
    cmd = """
    SELECT task_""" + info_category + """
    FROM tasks
    WHERE task_id = %s
    """
    args = (task_id,)
    return database_read(cmd, args)


def get_task(user_email):
    cmd = """
    SELECT t.*
    FROM tasks t
    JOIN users u ON t.user_email = u.user_email
    WHERE u.user_email = %s
    """
    args = (user_email,)
    return database_read(cmd, args, False)


file_name = 'task_system.py'
# print(add_task('test', True, 'ddd', 'ddd', datetime.now()))
print(get_task('test'))
