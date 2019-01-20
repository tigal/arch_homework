from behave import given, when, then

standard_end = "Push start task when you start this task. Push end task when you end it."


@given("new message or email arrived")
def given_assistant_gets_message(context):
    pass

@given("assistant asks if {something}")
def given_assistant_asks_if(context, something):
    context.task = something.lower()

@given("assistant ends similar tasks searching")
def given_similar_tasks(context):
    pass

@given("user wants to add task manually")
def given_add_task_manually(context):
    context.task = "user wants to add task manually"

@given("assistant tries to connect to the internet")
def given_tries_internet_connection(context):
    pass

@when("assistant finds there a task")
def when_task_found(context):
    context.message = "from Alice to do homework at 10.00 at Alice house"
    context.response = "You get message from Alice to do homework at 10.00 at Alice house. Add this task to list?"

@when('user says {command}')
def when_user_says_command(context, command):
    context.user_input = command.lower()

@when('assistant processes input')
def when_ass_process_input(context):
    if context.user_input == u'"yes"':
        if context.task == u'user wants to add new task from received message' or context.task == u'user wants to add task manually':
          context.response = "Do you want to know how long this task will take to do?"
    elif context.user_input == u'"no"':
        if context.task == u'user wants to know task duration' or context.task == u'user wants to find similar tasks in internet':
            context.response = standard_end
    else:
        context.response = "error"

@when("similar tasks are {found} in {where}")
def when_ass_ends_search(context, found, where):
    context.task = "similar tasks are "+found.lower()
    if found.lower() == u'not found':
        if where.lower() == u'base':
            context.response = "It is the first task of this type, I can't calculate its duration. \nDo you want to find similar tasks in internet?"
        else:
            context.response = "No similar tasks are found. \n"+standard_end

@when("user adds task {task}")
def when_user_adds_task(context, task):
    context.message = task
    context.user_input = u'"yes"'

@when("internet connection fails")
def when_internet_connection_fails(context):
    context.response = "Can't connect to the internet. Do you want retry?"

@then("assistant adds new task with proper tags")
def then_add_new_task(context):
    print("\nASSISTANT REPLIES: New task added")

@then('assistant says {answer}')
def then_assistant_replies(context, answer):
   print("\nASSISTANT REPLIES: " + context.response)

@then('assistant exits')
def then_ass_exits(context):
    print("\nASSISTANT REPLIES: Quiting...")

@then('assistant searches for the similar tasks in {where}')
def then_ass_searches(context, where):
    print("\nASSISTANT REPLIES: Searching...")

@then("assistant calculates average task duration")
def then_avg(context):
    context.response = "You will need 15 minutes. \n"+standard_end

