from datetime import (datetime, timedelta, date, time)
from database import *


class TaskStatus(str):
    PENDING = 'pending'
    UNDERWAY = 'underway'
    COMPLETED = 'completed'
    EXPIRED = 'expired'


class TaskVital(int):
    TRIVIAL = 0
    NORMAL = 1
    CRUCIAL = 2


class TaskTimePeriod(str):
    MORNING = 'morning'
    AFTERNOON = 'afternoon'
    EVENING = 'evening'


class TaskSchedule:
    def __init__(self, task, task_time_period, task_time):
        self.task = task
        self.task_time_period = task_time_period  # TaskTimePeriod
        self.task_time = task_time  # TimeDelta(min)

    def __str__(self):
        return f'task.task_id: {self.task.task_id}\n' \
               f'task_time_period: {self.task_time_period}\n' \
               f'task_time: {self.task_time}\n'


class Task:

    def __init__(self, user_email, **kwargs):
        self.task_id = kwargs.get('task_id', 0)
        self.user_email = user_email
        self.daily_task_id = kwargs.get('daily_task_id', 0)
        self.task_status = kwargs.get('task_status', TaskStatus.PENDING)
        self.task_vital = kwargs.get('task_vital', TaskVital.TRIVIAL)
        self.task_title = kwargs.get('task_title', 'some_task')
        self.task_content = kwargs.get('task_content', '')
        self.task_tag = kwargs.get('task_tag', '其他')
        self.task_is_daily = kwargs.get('task_is_daily', 0)
        self.task_start_time = kwargs.get('task_start_time', datetime.now())
        self.task_end_time = kwargs.get('task_end_time', datetime.now() + timedelta(days=10))
        self.task_duration_time = kwargs.get('task_duration_time', timedelta(hours=10))
        self.task_elapsed_time = kwargs.get('task_elapsed_time', 0)

    def __str__(self):
        return f'task_id: {self.task_id}\n' \
               f'user_email: {self.user_email}\n' \
               f'daily_task_id: {self.daily_task_id}\n' \
               f'task_status: {self.task_status}\n' \
               f'task_vital: {self.task_vital}\n' \
               f'task_title: {self.task_title}\n' \
               f'task_content: {self.task_content}\n' \
               f'task_tag: {self.task_tag}\n' \
               f'task_is_daily: {self.task_is_daily}\n' \
               f'task_start_time: {self.task_start_time}\n' \
               f'task_end_time: {self.task_end_time}\n' \
               f'task_duration_time: {self.task_duration_time}\n' \
               f'task_elapsed_time: {self.task_elapsed_time}\n'


def add_task(task):
    cmd = """
        INSERT INTO tasks (user_email, daily_task_id, task_status, task_vital,
        task_title, task_content, task_tag, task_is_daily, task_start_time, task_end_time, task_duration_time)
        VALUE (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)
        """
    args = (
        task.user_email, task.daily_task_id, task.task_status, task.task_vital, task.task_title, task.task_content,
        task.task_tag, task.task_is_daily, task.task_start_time, task.task_end_time, task.task_duration_time)
    return database_write(cmd, args)


def delete_task(*task_id):
    for item in task_id:
        if not delete("tasks", "task_id", item):
            return False
    return True


def reset_task_info(task_id, info_category, task_info):
    return reset_info("task", "task_id", task_id, info_category, task_info)


def add_elapsed_time(task_id, elapsed_time):
    cmd = """
    UPDATE tasks
    SET task_elapsed_time = ADDTIME(task_elapsed_time, %s)
    WHERE task_id = %s
    """
    args = (elapsed_time, task_id)
    return database_write(cmd, args)


def get_task_info(task_id, info_category):
    return get_info("task", "task_id", task_id, info_category)


def get_task(task_id):
    return get("tasks", "task_id", task_id)


def _get_task_objects_of_user_with_condition(user_email, condition_cmd='', condition_args=()):
    return _get_task_objects(join("tasks", "users", "user_email", user_email, condition_cmd, condition_args))


def get_task_object_of_user(user_email):
    return _get_task_objects_of_user_with_condition(user_email)


def modify_task(task):
    cmd = """
    UPDATE tasks
    SET task_status = %s, task_is_vital = %s, task_title = %s, task_content = %s, \
    task_start_time = %s, task_end_time = %s, task_deadline = %s
    WHERE task_id = %s
    """
    args = (
        task.task_status, task.task_vital, task.task_title, task.task_content, task.task_start_time,
        task.task_end_time,
        task.task_deadline, task.task_id)
    return database_write(cmd, args)


def get_tasks_date(user_email, date):
    return _get_task_objects_of_user_with_condition(user_email, 'AND DATE(t.task_start_time) = %s', (date,))


def get_task_objects_of_user_with_status_in_date(user_email, date, status):
    condition_cmd = """
    AND DATE(t.task_start_time) <= %s 
    AND DATE(t.task_end_time) >= %s 
    AND t.task_status = %s
    """
    return _get_task_objects_of_user_with_condition(user_email, condition_cmd, (date, date, status))


def get_tasks_status(user_email, status):
    condition_cmd = 'AND t.task_status = %s'
    return _get_task_objects_of_user_with_condition(user_email, condition_cmd, (status,))


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
    tasks = get_task_objects_of_user_with_status_in_date(user_email, date, TaskStatus.COMPLETED)
    task_num = len(tasks)
    duration_sum = sum([(_.task_end_time - _.task_start_time).total_seconds() / 3600 for _ in tasks])
    return task_num, duration_sum


def _get_task_objects(data):
    result = []
    for line in data:
        result.append(
            Task(line[1], task_id=line[0], daily_task_id=line[2], task_status=line[3], task_vital=line[4],
                 task_title=line[5], task_content=line[6], task_tag=line[7], task_is_daily=line[8],
                 task_start_time=line[9], task_end_time=line[10], task_duration_time=line[11],
                 task_elapsed_time=line[12]))
    return result


def get_task_schedule_objects(user_email, morning_time, afternoon_time, evening_time):
    # 处理时间
    morning_time = timedelta(hours=morning_time)
    afternoon_time = timedelta(hours=afternoon_time)
    evening_time = timedelta(hours=evening_time)
    current_date = datetime.today()

    # 获取任务列表
    task_objects_list = get_task_objects_of_user_with_status_in_date(user_email, current_date, TaskStatus.UNDERWAY)
    task_objects_list.sort(key=lambda x: (x.task_end_time, -x.task_vital), reverse=True)

    # 规划日程
    task_schedule_list = []
    while (morning_time or afternoon_time or evening_time) and task_objects_list:
        task = task_objects_list.pop()

        task_time = min([_get_time(TaskTimePeriod.MORNING, task), morning_time])
        if task_time:
            task_schedule_list.append(TaskSchedule(task, TaskTimePeriod.MORNING, task_time))
            task.task_elapsed_time += task_time
            morning_time -= task_time

        task_time = min([_get_time(TaskTimePeriod.AFTERNOON, task), afternoon_time])
        if task_time:
            task_schedule_list.append(TaskSchedule(task, TaskTimePeriod.AFTERNOON, task_time))
            task.task_elapsed_time += task_time
            afternoon_time -= task_time

        task_time = min([_get_time(TaskTimePeriod.EVENING, task), evening_time])
        if task_time:
            task_schedule_list.append(TaskSchedule(task, TaskTimePeriod.EVENING, task_time))
            task.task_elapsed_time += task_time
            evening_time -= task_time

    return task_schedule_list


def _get_time(task_time_period, task):
    # 上午: 6:00 - 12:00; 下午: 12:00 - 18:00; 晚上: 18:00 - 23:30
    if task_time_period == TaskTimePeriod.MORNING:
        time_period_start = datetime.combine(date.today(), time(hour=6))
        time_period_end = datetime.combine(date.today(), time(hour=12))
    elif task_time_period == TaskTimePeriod.AFTERNOON:
        time_period_start = datetime.combine(date.today(), time(hour=12))
        time_period_end = datetime.combine(date.today(), time(hour=18))
    else:
        time_period_start = datetime.combine(date.today(), time(hour=18))
        time_period_end = datetime.combine(date.today(), time(hour=23, minute=30))
        
    start = max([time_period_start, task.task_start_time])
    end = min([time_period_end, task.task_end_time])

    return min([end - start, task.task_duration_time - task.task_elapsed_time])
