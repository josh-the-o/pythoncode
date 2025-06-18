print("===========triangle========")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end="    ")
    print()
print("========matrix=======")
for i in range(1, 11):
    for j in range(1, 11):
        print(j, end="  ")
    print()

print("==========triangle star========")
for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end="    ")
    print()

print("========matrix star=======")
for i in range(1, 11):
    for j in range(1, 11):
        print('*', end="  ")
    print()
