"""
PLP week one code challenge:
Objective: Learn how to get user input in python

"""
# get user input
name = input("What is your name: ")
age = input("Enter your age: ")
location = input("Where are you located: ")

# format using f-strings
to_print = f"Hello {name}, you are {age} years old and live in {location}."
# print the formatted string
print(to_print)
