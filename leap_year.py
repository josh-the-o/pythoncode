a=("You can check if a year is a leap year in this code")
print(a)

b=('The number you enter should have 4 numbers')
print(b)
allow_run = True
while allow_run:

    leap_year = int(input("Enter a year: "))
    if (leap_year % 4) == 0:
        if (leap_year % 100) == 0:
            if (leap_year % 400) == 0:
                print("{0} it is a leap year".format(leap_year))
            else:
             print("{0} it is not a leap year".format(leap_year))
        else:
            print("{0} it is a leap year".format(leap_year))
    else:
        print("{0} it is not a leap year".format(leap_year))

    allow_run = input("do you want to continue press a \n") == 'a'

print("Thank you for using this code")
