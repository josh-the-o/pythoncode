gg = "We are going to study tables, all you need to do is enter the number you wanted"
print(gg)

run = True
while run:
    number = int(input("Enter the number \n"))

    for table_output in range(1, 21):
        print(number, "x" , table_output , "=" , number*table_output , sep = "  ")

    run = input("If you wanna continue click on y \n") == 'y'

print("Thank you for using this application")
