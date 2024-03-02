"""
PLP week two code challenge:
Objective: Sets

"""

# accept user input to create 2 sets of ints
setX = set((input("Please, Enter a number of integers: ")))

# display set1
print("set#1: ", setX)
setY = set((input("Please, Enter another number of integers: ")))

# display set2
print("set#2: ", setY)

# create new set that keeps duplicates from the 2 sets
setZ = setX.intersection(setY)

# display the new set
print("Set with common elements: ", setZ)

# create new set that keeps non duplicates from the 2 sets
setW = setX.symmetric_difference(setY)

# display the new set
print("Set with non duplicate elements: ", setW)
