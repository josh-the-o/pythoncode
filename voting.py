g = "Here you will find cube root of a number"
print(g)

x = int(input("Enter an integer: "))
for i in range(0, abs(x) + 1):
    if i ** 3 == abs(x):
        break
if i ** 3 != abs(x):
    print(x, 'is not a perfect cube:(')
else:
    if x < 0:
        i = -i
    print('Cube root of ' + str(x) + ' is ' + str(i))






