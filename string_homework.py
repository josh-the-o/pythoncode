homework = "You have to do strings for homework"
print(homework)
homework = "this is a homework"
print(homework)
# multiline_string
# homework="""
#         you have to 
#         do strings 
#         for 
#         """
print(homework)

print(homework[-1])
print(homework[1])
print(homework[0])

for i in range(0, len(homework)):
    print(homework[i])

print(len(homework))
print(homework[17])
print(homework.upper())
print(homework.lower())
print(homework.capitalize())
homework = homework + "  today done"
print(homework)

homework = 'T' + homework[1:]
print(homework)
print(homework[2:])
print(homework[:2])

homework = homework[:5]
print(homework)

homework = 'python'
string_hw = homework[2:-1]
print(string_hw)
classed = 'classed'

print('e' in homework)
print('sed' in classed)

homework = 'python'
homework = (enumerate(homework))
print(homework)

first_name = 'Joshua'
print(first_name)
print(first_name, '\n', first_name)
print("I am  \x99\x65\x87 Joshua")
print(r"I am  \x99\x65\x87 Joshua")

order_name = "{}, {},".format('Joshua', 'Theophilus')
print("\n===========order_name=========")
print(order_name)
full_name = "Joshua Theophilus"
print(full_name)
age = "13"
print(age)
school = "SJBHS"

data = input('Enter a value')
print(data)
print(type(data))
pl = "Please give your details"
print(pl)

first_name = input("Enter your first name- \t")
last_name = input("Enter your last name- ")
age = int(input("Enter your age- \t"), 10)
school = input("enter your schools name- \t ")
number = input("type your mobile number- \t ")
bio = input('Type about yourself like the things you like ')

print('Full name = ', first_name, ' ', last_name)
print('your age=', age)
print('your school=', school)
print('your number=', number)
print('you like to=', bio)

print(age)
print('============input_number_modulus===========')
print(13 % 2)
list_ = (9, 5, 6, 8, 3, 7, 0, 1)
if 1 in list_:
    print("yes there is 1 in list:", list_)


def full_name(name, school):
    print(f"Hi your name is {name} and studying in {school}")


full_name(school=school, name=first_name + " " + last_name)


def name_(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


name_(age=13)


def bio_data(name, school, age, bio):
    print(f'You are {name}, studying in {school}, and {age} years old, and these are the things you like{bio}')


bio_data(name=first_name + '  ' + last_name, school=school, age=age, bio=bio)
