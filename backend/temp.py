


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

def update_tasks(user_email):
    return create_daily_task_copy_date(
        user_email, datetime.now().date()
    ) and update_task_status(user_email)




def update_task_status(user_email):
    cmd = """
    something
    """
    return database_write(cmd, (user_email,))


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
