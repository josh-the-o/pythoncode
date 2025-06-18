friends_list = []
print(friends_list)

friends_list = ["My friends friends_list"]
print(friends_list)

# friends_list of my friends in school

friends_list = "my friends at school"
print(friends_list)

friends_list = """
[Justin,
Ashish,
Macario,
Pranav,
Charan]
"""
print(friends_list)

# friends_list of friends at home

friends_list = "my friends at home"
print(friends_list)

friends_list = """
[Archit,
Rithwick,
Prajwal,
Abhishek,
Sonu,
Shreerem]
"""
print(friends_list)

# best friends friends_list

friends_list = "My best friends"
print(friends_list)

friends_list = ["Shreeram", "Justin8.9", "Macario89j", ["Ashish2d"]]
print(friends_list)

print(friends_list[1])
print(friends_list[0])
print(friends_list[0][3])
print(len(friends_list))

# add data to the friends_list
friends_list.append("Jonathan")
print(friends_list)

# modify the data
friends_list[0] = 100
print(friends_list)

# removing friends_list
friends_list.remove(100)
print(friends_list)

print("=======These are few of my friends========")
print("=======I have more but I dont need to time to mention them=======")

for data in friends_list:
    print(str(data))

friends_list.pop(3)

for data in friends_list:
    print(str(data))
