username = input("Enter name")
print(username)

special_char = "@!#$%^&*():<>?~`"

password = input("Enter password")

if len(password)<8:
        print("insufficient characters")

else:
    for i in password:
        if i not in special_char:
            print("there are no special characters")
            break

        elif not (i.isdigit()):
             print("there are no numbers in the password")
            break

        elif i == "!":
            print("no exclamation marks allowed in password")
            break

        elif not(i.isupper()):
            print("Need upper character too")
            break
    
        else:
            print("password succesfully updated")