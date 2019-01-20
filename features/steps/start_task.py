from behave import given, when, then

def start_timer():
    pass

def stop_timer():
    pass

@given("user wants to start task")
def given_user_starts_task(context):
    context.task_timer_start = True

@given("user started task and wants to stop it")
def given_user_stops_task(context):
    context.task_timer_start = False

@when("user pushes {task_name}")
def user_pushes_task(context, task_name):
    context.current_task_name = task_name

@then("timer {action}")
def then_timer_do_smthg(context, action):
    if context.task_timer_start is True:
        start_timer()
        context.response = "Timing of " + context.current_task_name + " task started..."
    else:
        stop_timer()
        context.response = "Timing of " + context.current_task_name + " task ended... \nIt took 3 hours."