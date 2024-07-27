from datetime import datetime, timedelta, time
from enum import Enum

from backend.user_system import *


class TaskStatus(str):
    PENDING = "pending"
    UNDERWAY = "underway"
    COMPLETED = "completed"
    EXPIRED = "expired"


class TaskVital(int):
    TRIVIAL = 0
    NORMAL = 1
    CRUCIAL = 2


def get_task_vital(task_vital_str):
    if task_vital_str == "不重要":
        return TaskVital.TRIVIAL
    elif task_vital_str == "一般重要":
        return TaskVital.NORMAL
    else:
        return TaskVital.CRUCIAL


class TaskTimePeriod(Enum):
    MORNING = 0
    AFTERNOON = 1
    EVENING = 2

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value


class TaskSchedule:
    def __init__(self, task, task_time_period, task_time):
        self.task = task
        self.task_time_period = task_time_period  # TaskTimePeriod 上午/下午/晚上
        self.task_time = task_time  # TimeDelta(min) 任务持续时间

    def __str__(self):
        return (
            f"task.task_id: {self.task.task_id}\n"
            f"task_time_period: {self.task_time_period}\n"
            f"task_time: {self.task_time}\n"
        )


class Task:

    def __init__(self, user_email, **kwargs):
        self.task_id = kwargs.get("task_id", 0)
        self.user_email = user_email
        self.daily_task_id = kwargs.get("daily_task_id", 0)
        self.task_status = kwargs.get("task_status", TaskStatus.PENDING)
        self.task_vital = kwargs.get("task_vital", TaskVital.TRIVIAL)
        self.task_title = kwargs.get("task_title", "some_task")
        self.task_content = kwargs.get("task_content", "")
        self.task_tag = kwargs.get("task_tag", "其他")
        self.task_is_daily = kwargs.get("task_is_daily", 0)
        self.task_start_time = kwargs.get("task_start_time", datetime.now())
        self.task_end_time = kwargs.get(
            "task_end_time", datetime.now() + timedelta(days=10)
        )
        self.task_duration_time = kwargs.get("task_duration_time", timedelta(hours=10))
        self.task_elapsed_time = kwargs.get("task_elapsed_time", 0)
        self.task_complete_time = kwargs.get("task_complete_time", None)
        self.task_pic_url = kwargs.get("task_pic_url", None)

    def __str__(self):
        return (
            f"task_id: {self.task_id}\n"
            f"user_email: {self.user_email}\n"
            f"daily_task_id: {self.daily_task_id}\n"
            f"task_status: {self.task_status}\n"
            f"task_vital: {self.task_vital}\n"
            f"task_title: {self.task_title}\n"
            f"task_content: {self.task_content}\n"
            f"task_tag: {self.task_tag}\n"
            f"task_is_daily: {self.task_is_daily}\n"
            f"task_start_time: {self.task_start_time}\n"
            f"task_end_time: {self.task_end_time}\n"
            f"task_duration_time: {self.task_duration_time}\n"
            f"task_elapsed_time: {self.task_elapsed_time}\n"
            f"task_complete_time: {self.task_complete_time}\n"
            f"task_pic_url: {self.task_pic_url}\n"
        )


class DailyTask:
    def __init__(self, user_email, **kwargs):
        self.user_email = user_email
        self.daily_task_id = kwargs.get("daily_task_id", 0)
        self.daily_task_vital = kwargs.get("daily_task_vital", TaskVital.TRIVIAL)
        self.daily_task_title = kwargs.get("daily_task_title", "some_task")
        self.daily_task_content = kwargs.get("daily_task_content", "")
        self.daily_task_tag = kwargs.get("daily_task_tag", "其他")
        self.daily_task_start_date = kwargs.get(
            "daily_task_start_date", datetime.today().date()
        )
        self.daily_task_end_date = kwargs.get(
            "daily_task_end_date", datetime.today().date()
        )
        self.daily_task_start_time = kwargs.get(
            "daily_task_start_time", datetime.today().time()
        )
        self.daily_task_end_time = kwargs.get(
            "daily_task_end_time", datetime.today().time()
        )
        self.daily_task_duration_time = kwargs.get(
            "daily_task_duration_time", timedelta(hours=10)
        )
        self.daily_task_elapsed_time = kwargs.get("daily_task_elapsed_time", 0)
        self.daily_task_pic_url = kwargs.get("daily_task_pic_url", None)

    def __str__(self):
        return (
            f"user_email: {self.user_email}\n"
            f"daily_task_id: {self.daily_task_id}\n"
            f"daily_task_vital: {self.daily_task_vital}\n"
            f"daily_task_title: {self.daily_task_title}\n"
            f"daily_task_content: {self.daily_task_content}\n"
            f"daily_task_tag: {self.daily_task_tag}\n"
            f"daily_task_start_date: {self.daily_task_start_date}\n"
            f"daily_task_end_date: {self.daily_task_end_date}\n"
            f"daily_task_start_time: {self.daily_task_start_time}\n"
            f"daily_task_end_time: {self.daily_task_end_time}\n"
            f"daily_task_duration_time: {self.daily_task_duration_time}\n"
            f"daily_task_elapsed_time: {self.daily_task_elapsed_time}\n"
            f"daily_task_pic_url: {self.daily_task_pic_url}\n"
        )

    def to_normal_task(self, date):
        normal_task = Task(
            self.user_email,
            daily_task_id=self.daily_task_id,
            task_vital=self.daily_task_vital,
            task_title=self.daily_task_title,
            task_content=self.daily_task_content,
            task_tag=self.daily_task_tag,
            task_duration_time=self.daily_task_duration_time,
            task_elapsed_time=self.daily_task_elapsed_time,
            task_start_time=datetime.combine(date, self.daily_task_start_time),
            task_end_time=datetime.combine(date, self.daily_task_end_time),
            task_is_daily=1,
            task_pic_url=self.daily_task_pic_url,
        )
        return normal_task


# 增
def add_task(task):
    cmd = """
        INSERT INTO tasks (user_email, daily_task_id, task_status, task_vital,
        task_title, task_content, task_tag, task_is_daily, task_start_time, task_end_time, task_duration_time, task_elapsed_time, task_complete_time, task_pic_url)
        VALUE (%s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    args = (
        task.user_email,
        task.daily_task_id,
        task.task_status,
        task.task_vital,
        task.task_title,
        task.task_content,
        task.task_tag,
        task.task_is_daily,
        task.task_start_time,
        task.task_end_time,
        task.task_duration_time,
        task.task_elapsed_time,
        task.task_complete_time,
        task.task_pic_url,
    )
    return database_write(cmd, args)


# 删
def delete_task(*task_id):
    for item in task_id:
        if not delete("tasks", "task_id", item):
            return False
    return True


# 改
def reset_task_info(task_id, info_category, task_info):
    return reset_info("task", "task_id", task_id, info_category, task_info)


def reset_task(task):
    cmd = """
    UPDATE tasks
    SET task_status = %s, task_vital = %s, task_title = %s, task_content = %s, task_tag = %s, \
    task_start_time = %s, task_end_time = %s, task_duration_time = %s,task_elapsed_time =%s, \
    task_complete_time = %s, task_pic_url = %s
    WHERE task_id = %s
    """
    args = (
        task.task_status,
        task.task_vital,
        task.task_title,
        task.task_content,
        task.task_tag,
        task.task_start_time,
        task.task_end_time,
        task.task_duration_time,
        task.task_elapsed_time,
        task.task_complete_time,
        task.task_pic_url,
        task.task_id,
    )
    return database_write(cmd, args)


def add_work_time(task, work_time):
    if task.task_elapsed_time + work_time < task.task_duration_time:
        cmd = """
        UPDATE tasks
        SET task_elapsed_time = ADDTIME(task_elapsed_time, %s)
        WHERE task_id = %s
        """
        args = (work_time, task.task_id)
        database_write(cmd, args)
    else:
        task_is_complete(task)


# 查
def get_task_info(task_id, info_category):
    return get_info("task", "task_id", task_id, info_category)


def get_task(task_id):
    return get("tasks", "task_id", task_id)


def _get_task_objects(data):
    result = []
    for line in data:
        result.append(
            Task(
                line[1],
                task_id=line[0],
                daily_task_id=line[2],
                task_status=line[3],
                task_vital=line[4],
                task_title=line[5],
                task_content=line[6],
                task_tag=line[7],
                task_is_daily=line[8],
                task_start_time=line[9],
                task_end_time=line[10],
                task_duration_time=line[11],
                task_elapsed_time=line[12],
                task_complete_time=line[13],
                task_pic_url=line[14],
            )
        )
    return result


def _get_task_objects_of_user_with_condition(
        user_email, condition_cmd="", condition_args=()
):
    update_tasks(user_email)
    return _get_task_objects(
        join("tasks", "users", "user_email", user_email, condition_cmd, condition_args)
    )


def get_task_object_of_user(user_email):
    return _get_task_objects_of_user_with_condition(user_email)


def get_task_objects_of_user_in_date(user_email, some_date):
    condition_cmd = """
    AND DATE(t.task_start_time) <= %s 
    AND DATE(t.task_end_time) >= %s 
    """
    return _get_task_objects_of_user_with_condition(
        user_email, condition_cmd, (some_date, some_date)
    )


def get_tasks_of_user_with_status(user_email, status):
    condition_cmd = "AND t.task_status = %s"
    return _get_task_objects_of_user_with_condition(
        user_email, condition_cmd, (status,)
    )


def get_task_objects_of_user_with_status_in_date(user_email, some_date, status):
    condition_cmd = """
    AND DATE(t.task_start_time) <= %s 
    AND DATE(t.task_end_time) >= %s 
    AND t.task_status = %s
    """
    return _get_task_objects_of_user_with_condition(
        user_email, condition_cmd, (some_date, some_date, status)
    )


def get_task_objects_of_user_completed_in_date(user_email, some_date):
    condition_cmd = """
        AND DATE(t.task_complete_time) = %s 
        """
    return _get_task_objects_of_user_with_condition(
        user_email, condition_cmd, (some_date,)
    )


def get_complete_task_sum_in_date(user_email, some_date):
    return len(
        get_task_objects_of_user_completed_in_date(user_email, some_date)
    )


def get_work_time_sum_in_date(user_email, some_date):
    task_complete_list = get_task_objects_of_user_completed_in_date(user_email, some_date)
    task_underway_list = get_task_objects_of_user_with_status_in_date(
        user_email, some_date, TaskStatus.UNDERWAY
    )
    time_sum = timedelta(days=0)

    for task in task_complete_list:
        time_sum += task.task_duration_time

    for task in task_underway_list:
        time_sum += task.task_elapsed_time

    return time_sum


def get_complete_task_sum(user_email):
    return len(get_tasks_of_user_with_status(user_email, TaskStatus.COMPLETED))


def get_work_time_sum(user_email):
    task_complete_list = get_tasks_of_user_with_status(user_email, TaskStatus.COMPLETED)
    task_underway_list = get_tasks_of_user_with_status(user_email, TaskStatus.UNDERWAY)
    time_sum = timedelta(days=0)

    for task in task_complete_list:
        time_sum += task.task_duration_time

    for task in task_underway_list:
        time_sum += task.task_elapsed_time

    return time_sum


def get_average_work_time(user_email):
    date_sum = (
            date.today() - get_user_info(user_email, "register_date") + timedelta(days=1)
    )
    return get_work_time_sum(user_email) / date_sum.days


def get_week_report_of_user(user_email):
    complete_task_list = get_tasks_of_user_with_status(user_email, TaskStatus.COMPLETED)
    complete_task_list.sort(key=lambda x: x.task_complete_time)
    print_list(complete_task_list)

    this_week_start = date.today() - timedelta(days=date.today().weekday())

    week_report = []
    for delta in range(0, 7):
        week_date = this_week_start + timedelta(days=delta)
        week_report.append(
            len(list(filter(lambda obj: obj.task_complete_time.date() == week_date, complete_task_list))))

    return week_report


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

    return max(
        [
            min([end - start, task.task_duration_time - task.task_elapsed_time]),
            timedelta(0),
        ]
    )


def get_task_schedule_objects(user_email, morning_time, afternoon_time, evening_time):
    # 处理时间
    morning_time = timedelta(hours=morning_time)
    afternoon_time = timedelta(hours=afternoon_time)
    evening_time = timedelta(hours=evening_time)
    current_date = date.today()

    # 获取任务列表
    task_objects_list = get_task_objects_of_user_with_status_in_date(
        user_email, current_date, TaskStatus.UNDERWAY
    ) + get_task_objects_of_user_with_status_in_date(
        user_email, current_date, TaskStatus.PENDING
    )
    task_objects_list.sort(key=lambda x: (x.task_end_time, -x.task_vital), reverse=True)

    # 规划日程
    task_schedule_list = []
    while (morning_time or afternoon_time or evening_time) and task_objects_list:
        task = task_objects_list.pop()

        task_time = min([_get_time(TaskTimePeriod.MORNING, task), morning_time])
        if task_time:
            task_schedule_list.append(
                TaskSchedule(task, TaskTimePeriod.MORNING, task_time)
            )
            task.task_elapsed_time += task_time
            morning_time -= task_time

        task_time = min([_get_time(TaskTimePeriod.AFTERNOON, task), afternoon_time])
        if task_time:
            task_schedule_list.append(
                TaskSchedule(task, TaskTimePeriod.AFTERNOON, task_time)
            )
            task.task_elapsed_time += task_time
            afternoon_time -= task_time

        task_time = min([_get_time(TaskTimePeriod.EVENING, task), evening_time])
        if task_time:
            task_schedule_list.append(
                TaskSchedule(task, TaskTimePeriod.EVENING, task_time)
            )
            task.task_elapsed_time += task_time
            evening_time -= task_time

    # 排序
    task_schedule_list.sort(key=lambda x: x.task_time_period)
    return task_schedule_list


# TODO: 未修改
def get_ordered_tasks_date(user_email, date):
    tasks_date = get_task_objects_of_user_in_date(user_email, date)
    return sorted(tasks_date, key=lambda x: x.task_start_time)


def get_task_completed_sum(user_email):
    tasks = get_tasks_of_user_with_status(user_email, TaskStatus.COMPLETED)
    task_num = len(tasks)
    duration_sum = sum(
        [(_.task_end_time - _.task_start_time).total_seconds() / 3600 for _ in tasks]
    )
    workday_num = len(
        set(
            [
                _.task_start_time.date()
                for _ in tasks
                if _.task_start_time.month == datetime.today().month
            ]
        )
    )
    return task_num, duration_sum, duration_sum / workday_num


def get_task_completed_date(user_email, date):
    tasks = get_task_objects_of_user_with_status_in_date(
        user_email, date, TaskStatus.COMPLETED
    )
    task_num = len(tasks)
    duration_sum = sum(
        [(_.task_end_time - _.task_start_time).total_seconds() / 3600 for _ in tasks]
    )
    return task_num, duration_sum


def _get_daily_task_objects(data):
    result = []
    for line in data:
        temp = datetime.combine(datetime.today().date(), datetime.min.time())
        daily_task = DailyTask(
            user_email=line[1],
            daily_task_id=line[0],
            daily_task_vital=line[2],
            daily_task_title=line[3],
            daily_task_content=line[4],
            daily_task_tag=line[5],
            daily_task_start_date=line[6],
            daily_task_end_date=line[7],
            daily_task_start_time=(temp + line[8]).time(),
            daily_task_end_time=(temp + line[9]).time(),
            daily_task_duration_time=line[10],
            daily_task_elapsed_time=line[11],
            daily_task_pic_url=line[12],
        )
        result.append(daily_task)

    return result


def add_daily_task(daily_task):
    cmd = """
        INSERT INTO daily_tasks 
        (daily_task_id, user_email, daily_task_vital,
        daily_task_title, daily_task_content, daily_task_tag,
        daily_task_start_date, daily_task_end_date,
        daily_task_start_time, daily_task_end_time,
        daily_task_duration_time, daily_task_elapsed_time,
        daily_task_pic_url)
        VALUE (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    args = (
        daily_task.daily_task_id,
        daily_task.user_email,
        daily_task.daily_task_vital,
        daily_task.daily_task_title,
        daily_task.daily_task_content,
        daily_task.daily_task_tag,
        daily_task.daily_task_start_date,
        daily_task.daily_task_end_date,
        daily_task.daily_task_start_time,
        daily_task.daily_task_end_time,
        daily_task.daily_task_duration_time,
        daily_task.daily_task_elapsed_time,
        daily_task.daily_task_pic_url,
    )
    connection = database_connect()
    cursor = connection.cursor()
    cursor.execute(cmd, args)
    connection.commit()
    cursor.execute("SELECT LAST_INSERT_ID();")
    id = cursor.fetchone()[0]
    connection.close()
    daily_task.daily_task_id = id
    if not add_task(daily_task.to_normal_task(daily_task.daily_task_start_date)):
        return False
    return True


def delete_daily_task(*daily_task_id):
    for item in daily_task_id:
        if not delete("daily_tasks", "daily_task_id", item):
            return False
    return True


def _get_daily_task_objects_of_user_with_condition(
        user_email, condition_cmd="", condition_args=()
):
    return _get_daily_task_objects(
        join(
            "daily_tasks",
            "users",
            "user_email",
            user_email,
            condition_cmd,
            condition_args,
        )
    )


def get_daily_task_object(user_email, daily_task_id):
    condition_cmd = """
    AND daily_task_id = %s;
    """
    condition_args = (daily_task_id,)
    return _get_daily_task_objects_of_user_with_condition(
        user_email, condition_cmd, condition_args
    )


def get_daily_task_object_of_user(user_email):
    return _get_daily_task_objects_of_user_with_condition(user_email)


def get_daily_task_object_of_user_date(user_email, date):
    condition_cmd = """
    AND DATE(%s) BETWEEN DATE(daily_task_start_date) AND DATE(daily_task_end_date);
    """
    return _get_daily_task_objects_of_user_with_condition(
        user_email, condition_cmd=condition_cmd, condition_args=(date,)
    )


def create_daily_task_copy_date(user_email, date):
    daily_tasks_date = get_daily_task_object_of_user_date(user_email, date)
    for daily_task in daily_tasks_date:
        temp = daily_task.daily_task_start_date
        while temp <= date:
            if not is_daily_task_copy_exist(user_email, daily_task.daily_task_id, temp):
                if not add_task(daily_task.to_normal_task(temp)):
                    return False
            temp += timedelta(days=1)
        if temp <= daily_task.daily_task_end_date:
            if daily_task.daily_task_end_time < datetime.now().time():
                if not is_daily_task_copy_exist(
                        user_email, daily_task.daily_task_id, temp
                ):
                    if not add_task(daily_task.to_normal_task(temp)):
                        return False
    return True


def get_daily_task_copy_status_date(user_email, daily_task_id, date):
    cmd = """
    SELECT task_status
    FROM tasks
    WHERE user_email = %s 
        AND task_is_daily = 1
        AND daily_task_id = %s
        AND DATE(task_start_time) = %s
    """
    args = (user_email, daily_task_id, date)
    return database_read(cmd, args)


def is_daily_task_copy_exist(user_email, daily_task_id, date):
    cmd = """
    SELECT EXISTS(
        SELECT 1
        FROM tasks
        WHERE user_email = %s 
            AND task_is_daily = 1 
            AND daily_task_id = %s 
            AND DATE(task_start_time) = DATE(%s)
    )As task_exists
    """
    args = (user_email, daily_task_id, date)
    result = database_read(cmd, args)
    # print(result)
    return result


def update_tasks(user_email):
    return create_daily_task_copy_date(
        user_email, datetime.now().date()
    ) and update_task_status(user_email)


def update_task_status(user_email):
    cmd = """
    UPDATE tasks
    SET task_status = CASE
        WHEN NOW() < task_start_time THEN 'pending'
        WHEN NOW() > task_end_time AND task_status <> 'completed' THEN 'expired'
        WHEN NOW() BETWEEN task_start_time AND task_end_time AND task_status <> 'completed' THEN 'underway'
        WHEN task_status = 'completed' THEN 'completed'
        ELSE 'pending'
    END
    WHERE user_email = %s
    """
    return database_write(cmd, (user_email,))


def task_is_complete(task):
    reset_task_info(task.task_id, "status", TaskStatus.COMPLETED)
    reset_task_info(task.task_id, "complete_time", datetime.now())
    if task.task_is_daily:
        daily_task = get_daily_task_object(task.user_email, task.daily_task_id)[0]
        if daily_task.daily_task_end_date > date.today():
            if not is_daily_task_copy_exist(
                    task.user_email,
                    daily_task.daily_task_id,
                    date.today() + timedelta(days=1),
            ):
                task = daily_task.to_normal_task(date.today() + timedelta(days=1))
                add_task(task)


def reset_daily_task(daily_task):
    cmd = """
        UPDATE daily_tasks 
        SET
        daily_task_vital = %s,\
        daily_task_title = %s, daily_task_content = %s, daily_task_tag = %s,\
        daily_task_start_date = %s, daily_task_end_date = %s,\
        daily_task_start_time = %s, daily_task_end_time = %s,\
        daily_task_duration_time = %s, daily_task_elapsed_time = %s,\
        daily_task_pic_url = %s
        WHERE daily_task_id = %s
        """
    args = (
        daily_task.daily_task_vital,
        daily_task.daily_task_title,
        daily_task.daily_task_content,
        daily_task.daily_task_tag,
        daily_task.daily_task_start_date,
        daily_task.daily_task_end_date,
        daily_task.daily_task_start_time,
        daily_task.daily_task_end_time,
        daily_task.daily_task_duration_time,
        daily_task.daily_task_elapsed_time,
        daily_task.daily_task_pic_url,
        daily_task.daily_task_id,
    )
    return database_write(cmd, args)


def modify_task_pic_url(task, pic_url):
    pic_name = pic_url.split("/")[-1]
    temp = str(task.user_email) + "/task_pic/" + str(task.task_id) + "_" + pic_name
    bucket.put_object_from_file(temp, pic_url)
    pic_url = "https://foolish-han.oss-cn-beijing.aliyuncs.com/" + temp
    task.task_pic_url = pic_url


def modify_daily_task_pic_url(daily_task, pic_url):
    pic_name = pic_url.split("/")[-1]
    temp = (
            str(daily_task.user_email)
            + "/daily_task_pic/"
            + str(daily_task.daily_task_id)
            + "_"
            + pic_name
    )
    bucket.put_object_from_file(temp, pic_url)
    pic_url = "https://foolish-han.oss-cn-beijing.aliyuncs.com/" + temp
    daily_task.daily_task_pic_url = pic_url
