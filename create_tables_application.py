"""
To develop table application

1) Create function to display welcome message
2) Create function to display table input to be provided
3) Create function to get table detail
4) Create function to print table
5) Create function to ask user do you want print some more tables
6) Create function to display thank you message
7) Create function to run table application
    a) Call welcome message function
    b) Loop the below function but last function
    c) call function to display table input provided
    d) call function to get table input from the user
    e) call the function to print with user input
    f) call the function to the user to ask he wants to print any more table
        if yes
            repeat step c
        else
            stop the loop
    g) call the thank you message function
8) Stop the application
"""


# 1) Create function to display welcome message

def welcome():
    print('Welcome, in this application you can get the table you want to study')


# 2) Create function to display table input to be provided


def display_message():
    print('Enter the table you want to study')


# 3 ) Create function to get table detail


def enter_table():
    return int(input('Enter a table'))


# 4) Create function to print table
def print_table(table_value):
    for table_run in range(1, 11):
        print(table_value, "x", table_run, "=", table_value * table_run, sep="  ")


# 5 ) Create function to ask user do you want print some more tables
def continue_message():
    print("Do you want to continue?")
    return input("\t if yes press y\n") == "y"


# 6 ) Create function to display thank you message
def exit_message():
    print('Thank you for using this application ')


# 7 ) Create function to run table application
def run_table():
    run_table_ = True
    welcome()
    while run_table_:
        display_message()
        table_run = enter_table()
        print_table(table_run)
        run_table_ = continue_message()
    exit_message()


run_table()
