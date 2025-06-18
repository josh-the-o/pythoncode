"""
1. create function to display welcome message
2. create function to display user message
3. create a function to take user details
4. create a function to validate the age for voting
5. create a function to display a thank you
6. create a function to check person is available in the queue
7. create a function to run application
    a. call a function to display message
    b. call a function to user details
    c. call a function to  validate voters age
    d. call a function to ask where any person available in queue
        if yes
            continue the application
        else
            call a function to display thank you message and exit the application
"""


# 1. create function to display welcome message
def welcome_message():
    print("Welcome to voting validation application")


# 2. create function to display user message
def display_message():
    print("Enter user details to check voters age validity:\n")


# 3. create a function to take user details
def get_user_details():
    name = input("Enter user name:\n")
    age = int(input("Enter user age:\n"))
    return name, age


# 4. create a function to validate the age for voting
def validate_voting(age):
    return age >= 18


# 6. create a function to check person is available in the queue
def person_available():
    print("Is there any more person present in the queue")
    return input("\t if yes press y\n") == "y"


# 5. create a function to display a thank you
def say_thank_you():
    print("Thank you for using our voter application visit us next time")


# 7. create a function to run application
def run_application():
    let_run = True
    while let_run:
        display_message()
        name, age = get_user_details()
        eligible = validate_voting(age)
        if eligible:
            print(f"Hi {name}, you are eligible to vote")
        else:
            print(f"Hi {name}, you are not eligible to vote, since your age is below 18")
        let_run = person_available()
    say_thank_you()


run_application()
