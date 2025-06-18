import time

a = int(input("Enter the Principal\n"))
b = int(input("Enter the Rate%\n"))
c = int(input("Enter the Time in years\n"))

d = (f'The interest =', a * b * c / 100, "/-")
print(d)
time.sleep(3)

if c == 0:
    print("Not possible, try again")
    time.sleep(5)
else:
    print('the code has been executed successfully')

