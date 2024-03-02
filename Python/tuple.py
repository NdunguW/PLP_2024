"""
PLP week two code challenge:
Objective: Working with tuples

"""
# Method#1


# give variables to the books
BOOK1 = "The Subtle art of not giving a F^ck"
BOOK2 = "12 rules for life"
BOOK3 = "Atomic habits"
BOOK4 = "Shan zu: Art of War"
BOOK5 = "No More Mr Nice Guy"

# create the tuple
mytuple = tuple((BOOK1, BOOK2, BOOK3, BOOK4, BOOK5))

# display tuple
print("My book tuple is:", mytuple)

# iterate through a tuple
for i in mytuple:
    # display each book in a separate line
    print(i)


# Method#2

# get length of tuple
TUPLE_LENGTH = len(mytuple)

# display length
print("The length of my tuple is:", TUPLE_LENGTH)

# loop to display all books by referring to their index number
for x in range(TUPLE_LENGTH):
    print(mytuple[x])
