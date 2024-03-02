"""
PLP week two assignment:
Objective: Manipulating lists

"""
# create an empty list
my_list = []

# append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# display list
print("With appended elements: ", my_list)

# insert value at 2nd position
my_list.insert(1, 15)
print("Inserting a value at 2nd pos:", my_list)

# extend with another list
list2 = [50, 60, 70]
my_list.extend(list2)
print("Extend with another list: ", my_list)

# remove last element from list
my_list.pop()
print("Without the last element: ", my_list)

# sort list in ascending order
my_list.sort(reverse=False)
print("Sorted list in ascending order: ", my_list)

# find & display index of a value in the list
print("The index of value 30 is:", my_list.index(30))
