from datetime import datetime
from database import *


class TaskStatus(str):
    PENDING = 'pending'
    UNDERWAY = 'underway'
    COMPLETED = 'completed'
    EXPIRED = 'expired'


class Task:
    
    def __init__(self, user_email, **kwargs):
        self.id = kwargs.get('id', 0)
        self.user_email = user_email
        self.status = kwargs.get('status', TaskStatus.PENDING)
        self.is_vital = kwargs.get('is_vital', 0)
        self.title = kwargs.get('title', None)
        self.content = kwargs.get('content', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.deadline = kwargs.get('deadline', None)
        self.is_daily = kwargs.get('is_daily', 0)
        self.tag = kwargs.get('tag', None)
    
    def __str__(self):
        return f'task_id: {self.id}\t' \
               f'user_email: {self.user_email}\t' \
               f'status: {self.status}\t' \
               f'is_vital: {self.is_vital}\t' \
               f'title: {self.title}\t' \
               f'content: {self.content}\t' \
               f'start_time: {self.start_time}\t' \
               f'end_time: {self.end_time}\t' \
               f'deadline: {self.deadline}\t' \
               f'is_daily: {self.is_daily}\t' \
               f'tag: {self.tag}'


def add_task(task):
    cmd = """
    INSERT INTO tasks (user_email, task_status, task_is_vital,
    task_title, task_content, task_start_time, task_end_time, task_deadline,
    task_is_daily, task_tag)
    VALUE (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s)
    """
    args = (task.user_email, task.status, task.is_vital, task.title, task.content, task.start_time,
            task.end_time, task.deadline, task.is_daily, task.tag)
    return database_write(cmd, args)


def delete_task(*task_id):
    for item in task_id:
        if not delete("tasks", "task_id", item):
            return False
    return True


def reset_task_info(task_id, info_category, task_info):
    # info_category: status, is_vital, title, content, create_time, deadline, complete_time
    return reset_info("task", "task_id", task_id, info_category, task_info)


def get_task_info(task_id, info_category):
    # info_category: status, is_vital, title, content, create_time, deadline, complete_time
    return get_info("task", "task_id", task_id, info_category)


def get_tasks(user_email, condition_cmd='', condition_args=()):
    cmd = """
    SELECT t.*
    FROM tasks t
    JOIN users u ON t.user_email = u.user_email
    WHERE u.user_email = %s
    """ + condition_cmd
    args = (user_email,) + condition_args
    data = database_read(cmd, args, False)
    if not data:
        return False
    else:
        return get_task_objects(data)


def modify_task(task):
    cmd = """
    UPDATE tasks
    SET task_status = %s, task_is_vital = %s, task_title = %s, task_content = %s, \
    task_start_time = %s, task_end_time = %s, task_deadline = %s
    WHERE task_id = %s
    """
    args = (task.status, task.is_vital, task.title, task.content, task.start_time, task.end_time,
            task.deadline, task.id)
    return database_write(cmd, args)


def get_tasks_date(user_email, date):
    return get_tasks(user_email, 'AND DATE(t.task_start_time) = %s', (date,))


def get_tasks_date_status(user_email, date, status):
    condition_cmd = """AND DATE(t.task_start_time) = %s AND t.task_status = %s"""
    return get_tasks(user_email, condition_cmd, (date, status))


def get_tasks_status(user_email, status):
    condition_cmd = """AND t.task_status = %s"""
    return get_tasks(user_email, condition_cmd, (status,))


def get_ordered_tasks_date(user_email, date):
    tasks_date = get_tasks_date(user_email, date)
    return sorted(tasks_date, key=lambda x: x.start_time)


def update_tasks(user_email):
    return update_daily_task('task_deadline') and update_daily_task('task_end_time') and \
        update_daily_task('task_deadline') and update_task_status(user_email)


def update_daily_task(time):
    cmd = f"""
    UPDATE `tasks`
    SET {time} = CONCAT(
    DATE_FORMAT(CURDATE(), '%Y-%m-%d'),
    ' ',
    TIME({time})
    )
    WHERE DATE({time}) != CURDATE()  AND task_is_daily = TRUE;
    """
    return database_write(cmd)


def update_task_status(user_email):
    cmd = """
          UPDATE tasks
          SET task_status = 'expired'
          WHERE user_email = %s AND task_deadline < NOW() AND task_status != 'completed';
          """
    return database_write(cmd, (user_email,))


def get_task_completed_sum(user_email):
    tasks = get_tasks_status(user_email, TaskStatus.COMPLETED)
    task_num = len(tasks)
    duration_sum = sum([(_.end_time - _.start_time).total_seconds() / 3600 for _ in tasks])
    workday_num = len(
        set([_.start_time.date() for _ in tasks if _.start_time.month == datetime.today().month]))
    return task_num, duration_sum, duration_sum / workday_num


def get_task_completed_date(user_email, date):
    tasks = get_tasks_date_status(user_email, date, TaskStatus.COMPLETED)
    task_num = len(tasks)
    duration_sum = sum([(_.end_time - _.start_time).total_seconds() / 3600 for _ in tasks])
    return task_num, duration_sum


def get_task_objects(data):
    result = []
    for line in data:
        result.append(
            Task(line[1], id=line[0], status=line[2], is_vital=line[3],
                 title=line[4], content=line[5],
                 start_time=line[6], end_time=line[7], deadline=line[8],
                 is_daily=line[9], tag=line[10]))
    return result


def print_list(lis):
    for item in lis:
        print(item)
