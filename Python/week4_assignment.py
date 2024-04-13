"""
PLP week four assignment:
Objective: OOP in Python
"""


# create a python class named Person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # prints a message introducing a person
        print(f"This is {self.name}, a {self.age} years old {self.gender}.")


# create instance of the Person class
person = Person("William", 24, "Male")

# calling the introduce method to display the person's information
person.introduce()

"""
This code defines a Person class with name, age, and gender attributes, 
and an introduce method that prints a message introducing the person. 
It also creates an instance of the Person class and calls the introduce method to display the information. 
Just replace “William”, 24, and “Male” with the actual details to use this class for any person.
"""