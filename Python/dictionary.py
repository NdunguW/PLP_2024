"""
PLP week two code challenge:
Objective: Using dictionary to store information

"""
# define keys in dictionary
person_info = {"name": " ", "age": " ", "favourite color": " "}

# join input values with keys
person_info["name"] = input("What is your name: ")
# age should be integer
person_info["age"] = int(input("How old are you now: "))
person_info["favourite color"] = input("Enter your favourite color: ")

# display dictionary
print(person_info)

# Also

# get user input from a person
names = input("What is your name: ")
years_old = int(input("How old are you now: "))
favcolor = input("Enter your favourite color: ")

# make the dictionary using dict() method
person_info = dict(name=names, age=years_old, color=favcolor)

# display the dictionary
print(person_info)
