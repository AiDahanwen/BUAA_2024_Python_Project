from datetime import datetime
from database import *
from task_system import *


class TaskRecord:

    def __init__(self, task, **kwargs):
        self.task_record_id = kwargs.get('task_record_id', 0)
        self.user_email = task.user_email
        self.task_id = task.id
        self.task_record_complete_time = kwargs.get('task_record_complete_time', datetime.now())

    def __str__(self):
        return f'task_record_id: {self.task_record_id}\t' \
               f'user_email: {self.user_email}\t' \
               f'task_id: {self.task_id}\t' \
               f'task_record_complete_time: {self.task_record_complete_time}\t'


def add_task_record(task_record):
    cmd = """
        INSERT INTO task_records (user_email, task_id, task_record_complete_time)
        VALUE (%s, %s, %s)
        """
    args = (task_record.user_email, task_record.task_id, task_record.task_record_complete_time)
    return database_write(cmd, args)


def delete_task_record(task_record_id):
    return delete("task_records", "task_record_id", task_record_id)


def reset_task_record_info(task_record_id, info_category, task_info):
    return reset_info("task_record", "task_record_id", task_record_id, info_category, task_info)


def get_task_record_info(task_record_id, info_category):
    return get_info("task_record", "task_record_id", task_record_id, info_category)


def get_task_record(task_record_id):
    return get("task_records", "task_record_id", task_record_id)


def get_task_record_objects(task_records):
    result = []
    for line in task_records:
        result.append(
            TaskRecord(Task(line[1], id=line[2]), task_record_id=line[0], task_record_complete_time=line[3]))
    return result
