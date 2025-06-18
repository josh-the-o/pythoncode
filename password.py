import os
import time
from tkinter import *

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == 'Joshua' and password == 'I am not a bot':
    time.sleep(1)
    print("Login successful!")
    print("Welcome to this webpage")
    time.sleep(2)

else:
    print("Password did not match!")
    print("You are not my master :(")
    time.sleep(2)
