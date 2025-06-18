"""
I will practice function here

In this function we can learn how to multiply and divide

steps:
1) make a welcome function
2) make a display message
3) Ask user to select an option as shown below
    a) press 1 to learn how to multiply
    b)press 2 to learn how to divide
4)Create a function to take user input
5)Create function for multiplication
6)Create function for division
7)Create function do you want to continue
8)Create a function do display exit message
9)Create a function to run application
    a)Call welcome message
    b)Call display function
    c)Call option function
    d)Call get user option function
    e)Compare the option
        1) if 1 call multiplication
        2)elif 2 call division
        3)else print you selected invalid option
    f)Call do you want to continue function
        1)if yes continue from step b
        2)else call thank you function and exit application

"""


def welcome_message():
    print('Welcome to this application here you can learn how to multiply and divide')


def display_message():
    print("Press 1 if you want to learn how to multiply and press 2 to learn how to divide")


def option_choose():
    return int(input('Choose a number'))


def multiplication():
    return print("An example of multiplying is that, eg you want to add 6+6+6+6+6, your answer will be 30, \n"
                 " but an easier way to add it is multiplying 6 by 5 times, so 5 times 6 = 30.\n"
                 "for example 2 x 2 = 4, you are adding in an easier way so now give me two numbers  and I "
                 "will give you the answer for it ")


def enter_input_for_operation():
    number_1 = int(input('enter first number'))
    number_2 = int(input('enter second number'))
    return number_1, number_2


def multiply_(number_1, number_2):
    print(f"product of {number_1}, {number_2} is {number_1 * number_2}")


def division():
    return print("So now in this we shall learn division. Eg:You have 10 chocolates and 5 friends"
                 " and you want to share equal amounts of chocolates to everyone, you will divide.\n"
                 " So now you have to use multiplication here, you have 5 friends and 10 chocolates"
                 " 5 x 2 = 10, so you have to give each person 2 chocolates to make it even.\n"
                 " Now give me 2 numbers of your choice and i will divide for you")


def divide(number_1, number_2):
    print(f"quotient of {number_1}, {number_2} is {number_1 / number_2}")


def continue_message():
    print("Do you want to continue")
    return input("\t if yes press y\n") == "y"


def exit_message():
    print('Thank you for using this application')


def run_application():
    learn_ = True
    welcome_message()
    while learn_:
        display_message()
        option = option_choose()
        if option <= 0 or option > 2:
            print('you have chosen invalid option')
        else:
            if 1 == option:
                multiplication()
                number_1, number_2 = enter_input_for_operation()
                multiply_(number_1, number_2)

            elif 2 == option:
                division()
                number_1, number_2 = enter_input_for_operation()
                divide(number_1, number_2)

        learn_ = continue_message()

    exit_message()


run_application()
