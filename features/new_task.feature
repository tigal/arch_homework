Feature: Add new task from mail or message
  Adding new tasks

  Scenario: Add new task from the received message
    Given new message or email arrived
     When assistant finds there a task
     Then assistant says "You get message from Alice to do homework at 10.00 at Alice house. Add this task to list?"

  Scenario: Add new task manually
    Given user wants to add task manually
     When user adds task "Do homework as Alice house today at 10.00"
      And assistant processes input
     Then assistant adds new task with proper tags
     Then assistant says "Do you want to know how long this task will take to do?"

  Scenario: User wants to add received task
    Given assistant asks if user wants to add new task from received message
     When user says "Yes"
      And assistant processes input
     Then assistant adds new task with proper tags
      And assistant says "Do you want to know how long this task will take to do?"

  Scenario: User don't want to add new task
    Given assistant asks if user wants to add new task from received message
     When user says “No"
      And assistant processes input
     Then assistant exits

  Scenario: User wants to know task duration
    Given assistant asks if user wants to know task duration
     When user says "Yes"
      And assistant processes input
     Then assistant searches for the similar tasks in base and collects them

  Scenario: User doesn't want to know task duration
    Given assistant asks if user wants to know task duration
     When user says "No"
      And assistant processes input
     Then assistant says "Push start task when you start this task. Push end task when you end it."

  Scenario: Similar tasks are found
    Given assistant ends similar tasks searching
     When similar tasks are found in base
     Then assistant calculates average task duration
      And assistant says "You will need 15 minutes. \nPush start task when you start this task. Push end task when you end it."

  Scenario: Similar tasks are not found
    Given assistant ends similar tasks searching
     When similar tasks are not found in base
     Then assistant says "It is the first task of this type, I can't calculate its duration. \nDo you want to find similar tasks in internet?"

  Scenario: User wants to find similar tasks in internet
    Given assistant asks if user wants to find similar tasks in internet
     When user says "Yes"
      And assistant processes input
     Then assistant searches for the similar tasks in internet and collects them

  Scenario: User doesn't want to find similar tasks in internet
    Given assistant asks if user wants to find similar tasks in internet
     When user says "No"
      And assistant processes input
     Then assistant says "Push start task when you start this task. Push end task when you end it."

  Scenario: Similar tasks in internet are not found
    Given assistant ends similar tasks searching
     When similar tasks are not found in internet
     Then assistant says "No similar tasks are found. \nPush start task when you start this task. Push end task when you end it."

  Scenario: Internet connection fails
    Given assistant tries to connect to the internet
     When internet connection fails
     Then assistant says "Can't connect to the internet. Do you want retry?"

