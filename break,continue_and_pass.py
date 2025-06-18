print("==============break function==========")
for i in range(1, 51):
    if i == 15:
        break
    print(i)

print("==============continue function==========")
for i in range(1, 51):
    if i in range(1, 25):
        continue
    print(i)

for i in range(1, 51):
    pass

