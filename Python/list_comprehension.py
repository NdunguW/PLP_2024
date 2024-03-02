"""
PLP week two code challenge:
Objective: list comprehension

"""
# a list storing words
myList = ["I", "You", "Family", "Them", "Python", "Power Learn"]

# display list
print("My List:", myList)

# with list comprehension to store the words with odd number of characters
oddList = [i for i in myList if (len(i) % 2 != 0)]

# display new list
print("New list with odd no. of characters: ", oddList)

"""
# Without list comprehension
# empty list to store the words with odd number of characters
oddList = []

# use a for statement with a conditional test inside
for i in myList:
    # print(len(i))
    if ((len(i) % 2 == 0)):
        print(i, "of char length", len(i), "is even")
    else:
        oddList.append(i)

print("New list with odd no. of characters: ", oddList)
"""
