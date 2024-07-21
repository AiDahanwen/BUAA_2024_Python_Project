from datetime import datetime, timedelta
from database import *


class TaskStatus(str):
    PENDING = 'pending'
    UNDERWAY = 'underway'
    COMPLETED = 'completed'
    EXPIRED = 'expired'


class Task:

    def __init__(self, user_email, **kwargs):
        self.task_id = kwargs.get('task_id', 0)
        self.user_email = user_email
        self.task_status = kwargs.get('task_status', TaskStatus.PENDING)
        self.task_is_vital = kwargs.get('task_is_vital', 0)
        self.task_title = kwargs.get('task_title', 'some_task')
        self.task_content = kwargs.get('task_content', None)
        self.task_description = kwargs.get('task_description')
        self.task_tag = kwargs.get('task_tag', None)
        self.task_is_daily = kwargs.get('task_is_daily', 0)
        self.task_start_time = kwargs.get('task_start_time', None)
        self.task_end_time = kwargs.get('task_end_time', None)
        self.task_deadline = kwargs.get('task_deadline', None)
        self.task_repeat_start_time = kwargs.get('task_repeat_start_time', None)
        self.task_repeat_end_time = kwargs.get('task_repeat_end_time', None)
        self.task_repeat_start_date = kwargs.get('task_repeat_start_date', None)
        self.task_repeat_end_date = kwargs.get('task_repeat_end_date', None)

    def __str__(self):
        return f'task_id: {self.task_id}\t' \
               f'user_email: {self.user_email}\t' \
               f'task_status: {self.task_status}\t' \
               f'task_is_vital: {self.task_is_vital}\t' \
               f'task_title: {self.task_title}\t' \
               f'task_content: {self.task_content}\t' \
               f'task_description: {self.task_description}\t' \
               f'task_tag: {self.task_tag}' \
               f'task_is_daily: {self.task_is_daily}' \
               f'task_start_time: {self.task_start_time}\t' \
               f'task_end_time: {self.task_end_time}\t' \
               f'task_deadline: {self.task_deadline}\t' \
               f'task_repeat_start_time: {self.task_repeat_start_time}' \
               f'task_repeat_end_time: {self.task_repeat_end_time}\t' \
               f'task_repeat_start_date: {self.task_repeat_start_date}\t' \
               f'task_repeat_end_date: {self.task_repeat_end_date}\t'


def add_task(task):
    if not task.task_is_daily:
        cmd = """
        INSERT INTO tasks (user_email, task_status, task_is_vital,
        task_title, task_content, task_description,task_tag, task_start_time, task_end_time, task_deadline)
        VALUE (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s)
        """
        args = (
            task.user_email, task.task_status, task.task_is_vital, task.task_title, task.task_content,
            task.task_description, task.task_tag, task.task_start_time, task.task_end_time, task.task_deadline)
    else:
        cmd = """
        INSERT INTO tasks (user_email, task_status, task_is_vital, task_title, task_content, task_description, 
        task_tag, task_is_daily, 
        task_repeat_start_time, task_repeat_end_time, task_repeat_start_date, task_repeat_end_date)
        VALUE (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        args = (
            task.user_email, task.task_status, task.task_is_vital, task.task_title, task.task_content,
            task.task_description, task.task_tag, task.task_is_daily,
            task.task_repeat_start_time, task.task_repeat_end_time,
            task.task_repeat_start_date, task.task_repeat_end_date)
    return database_write(cmd, args)


def delete_task(*task_id):
    for item in task_id:
        if not delete("tasks", "task_id", item):
            return False
    return True


def reset_task_info(task_id, info_category, task_info):
    return reset_info("task", "task_id", task_id, info_category, task_info)


def get_task_info(task_id, info_category):
    return get_info("task", "task_id", task_id, info_category)


def get_task(task_id):
    get("tasks", "task_id", task_id)


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
        return _get_task_objects(data)


def modify_task(task):
    cmd = """
    UPDATE tasks
    SET task_status = %s, task_is_vital = %s, task_title = %s, task_content = %s, \
    task_start_time = %s, task_end_time = %s, task_deadline = %s
    WHERE task_id = %s
    """
    args = (
        task.task_status, task.task_is_vital, task.task_title, task.task_content, task.task_start_time,
        task.task_end_time,
        task.task_deadline, task.task_id)
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
    return sorted(tasks_date, key=lambda x: x.task_start_time)


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
    duration_sum = sum([(_.task_end_time - _.task_start_time).total_seconds() / 3600 for _ in tasks])
    workday_num = len(
        set([_.task_start_time.date() for _ in tasks if _.task_start_time.month == datetime.today().month]))
    return task_num, duration_sum, duration_sum / workday_num


def get_task_completed_date(user_email, date):
    tasks = get_tasks_date_status(user_email, date, TaskStatus.COMPLETED)
    task_num = len(tasks)
    duration_sum = sum([(_.task_end_time - _.task_start_time).total_seconds() / 3600 for _ in tasks])
    return task_num, duration_sum


def _get_task_objects(data):
    result = []
    for line in data:
        result.append(
            Task(line[1], task_id=line[0], task_status=line[2], task_is_vital=line[3],
                 task_title=line[4], task_content=line[5], task_description=line[6],
                 task_tag=line[7], task_is_daily=line[8], task_start_time=line[9],
                 task_end_time=line[10], task_deadline=line[11], task_repeat_start_time=line[12],
                 task_repeat_end_time=line[13], task_repeat_start_date=line[14], task_repeat_end_date=line[15]))
    return result


print(add_task(Task("123", task_status=TaskStatus.UNDERWAY, task_is_vital=True, task_is_daily=1,
                    task_repeat_start_date=datetime.today(),
                    task_repeat_end_date=(datetime.today() + timedelta(10)))))
