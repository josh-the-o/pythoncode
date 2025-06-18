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

def welcome_msg():
    print("welcome to the voting validation application")

def display_msg():
    print("Enter you details to check if you are eligible to vote")

def details():
    name = input("Enter your full name:\n")
    age = int(input("Enter user age:\n"))
    return name, age

def voting(age):
    return age >= 18

def more_candidates():
    print("Are there more people in the queue? \n")
    return input("\t if yes click on y if not click on any other key \n") == 'y'

def thenks():
    print("Thank you for using this application, if you were under aged please come back when you are 18 or above :)")

def run_app():
    run = True
    while run:
        welcome_msg()
        display_msg()
        name, age = details()
        eligible = voting(age)
        if eligible:
            print(f"Hi {name}, you are eligible to vote")
        else:
            print(f"Hi {name}, you are not eligible to vote, since your age is below 18")

        run = more_candidates()
    thenks()

run_app()
