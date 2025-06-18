"""
1) Make a welcome message
2) Display message to user
3) Ask user to select an option as shown below
    a)press 1 for addition
    b)press 2 for subtraction
    c)press 3 for multiplication
    d)press 4 for division
4)Create a function to take user input
5)Create function for addition
6)Create function for subtraction
7)Create function for multiplication
8)Create function for division
9)Create function do you want to continue
10)Create a function do display exit message
11)Create a function to run application
    a)Call welcome message
    b)Call display function
    c)Call option function
    d)Call get user option function
    e)Compare the option
        1) if 1 call addition function
        2)elif 2 call subtraction function
        3)elif 3 call multiplication function
        4)elif 4 call division function
        5)else print you selected invalid option
    f)Call do you want to continue function
        1)if yes continue from step b
        2)else call thank you function and exit application
"""


def welcome():
    print('Welcome in this application you can find answers for addition, subtraction, multiplication and division')


def display_message():
    print('Choose one from the below')


def select():
    print("press 1 for addition, press 2 for subtraction, press 3 for multiplication and press 4 for ""division")


def choose():
    return int(input('Choose a number'))


def enter_input_for_operation():
    number_1 = int(input('enter first number'))
    number_2 = int(input('enter second number'))
    return number_1, number_2


def function_addition(number_1, number_2):
    print(f"sum of {number_1}, {number_2} is {number_1 + number_2}")


def function_subtraction(number_1, number_2):
    print(f"difference between {number_1}, {number_2} is {number_1 - number_2}")


def function_multiplication(number_1, number_2):
    print(f"product of {number_1}, {number_2} is {number_1 * number_2}")


def function_division(number_1, number_2):
    print(f"quotient of {number_1}, {number_2} is {number_1 / number_2}")


def continue_message():
    print("Do you want to continue")
    return input("\t if yes press y if no type in any other letter\n") == "y"


def exit_message():
    print('Thank you for using this application')


def run_application():
    let_run = True
    welcome()
    while let_run:
        display_message()
        select()
        options = choose()
        if options <= 0 or options > 4:
            print('you have chosen invalid option')
        else:
            number_1, number_2 = enter_input_for_operation()
            if 1 == options:
                function_addition(number_1, number_2)
            elif 2 == options:
                function_subtraction(number_1, number_2)
            elif 3 == options:
                function_multiplication(number_1, number_2)
            elif 4 == options:
                function_division(number_1, number_2)

        let_run = continue_message()
    exit_message()


run_application()
