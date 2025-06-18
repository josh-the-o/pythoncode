"""
   1) Make a welcome message"
   2) Display message to user"
   3) Ask user to select an option as shown below
        a) press 1 for Biriyani"
        b)press 2 for Pulao"
        c)press 3 for Chicken Colambu
        d)press 4 for Paneer
   4)Create a function to take user input
   5)Create function for Biriyani
   6)Create function for Pulao
   7)Create function for Chicken
   8)Create function for Paneer
   9)Create function do you want to continue
   10)Create a function do display exit message
   11)Create a function to run application
       a)Call welcome message
       b)Call display function
       c)Call option function
       d)Call get user option function
       e)Compare the option
   1) if 1 call  function Biriyani
   2)elif 2 call  function Pulao
   3)elif 3 call  function Chicken Colambu
   4)elif 4 call  function Paneer
   5)else print you selected invalid option
   f)Call do you want to continue function
   1)if yes continue from step b
   2)else call thank you function and exit application")
"""


# 1) Make a welcome message


def welcome_message():
    print("Welcome to this application I am going to teach you a few recipes")


# 2) Display message to user"


def display_message():
    print("Press 1 to learn how to cook Biriyani\n"
          "2 to learn Pulao\n"
          "3 to learn Chicken Curry\n"
          "4 to learn Paneer")


# 4 )Create a function to take user input


def options():
    return int(input("Choose a number"))


# 5 )Create function for Biriyani


def biriyani():
    print("Biriyani\n"
          "step1:\n"
          "step2:\n"
          "step3:\n"
          "step4:\n"
          "step5:\n"
          "step6:\n"
          "step7:\n"
          "step8:\n"
          "step9:\n"
          "step10:\n")


# 6 )Create function for Pulao


def pulao():
    print("Pulao\n"
          "step1:\n"
          "step2:\n"
          "step3:\n"
          "step4:\n"
          "step5:\n"
          "step6:\n"
          "step7:\n"
          "step8:\n"
          "step9:\n"
          "step10:\n")


# 7 )Create function for Chicken Colambu


def chicken_curry():
    print("Chicken curry\n"
          "step1:\n"
          "step2:\n"
          "step3:\n"
          "step4:\n"
          "step5:\n"
          "step6:\n"
          "step7:\n"
          "step8:\n"
          "step9:\n"
          "step10:\n")


# 8 )Create function for Paneer


def paneer():
    print("Paneer\n"
          "step1:\n"
          "step2:\n"
          "step3:\n"
          "step4:\n"
          "step5:\n"
          "step6:\n"
          "step7:\n"
          "step8:\n"
          "step9:\n"
          "step10:\n")


# 9 )Create function do you want to continue


def continue_message():
    print("Do you want to continue?")
    return input("\tIf yes press y\n") == "y"


# 10 )Create a function do display exit message


def exit_message():
    print('Thank you for using this application')


# 11 )Create a function to run application


def run_application():
    running = True
    welcome_message()
    while running:
        display_message()
        choosing = options()
        if choosing <= 0 or choosing > 4:
            print('you have chosen invalid option')
        else:
            if 1 == choosing:
                biriyani()

            elif 2 == choosing:
                pulao()

            elif 3 == choosing:
                chicken_curry()

            elif 4 == choosing:
                paneer()

        running = continue_message()

    exit_message()


run_application()
