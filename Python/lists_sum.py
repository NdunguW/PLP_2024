"""
PLP week two code challenge:
Objective: get user to create a list of integers then compute sum

"""

# empty list to store the numbers
numbers = []

# get input for 5 numbers
for i in range(5):
    num = int(input("Enter a number: "))

    # append the numbers to the empty list
    numbers.append(num)

# test
print("The list is:", numbers)

# calculate the sum of the numbers
get_sum = sum(numbers)
# display sum
print("The sum is:", get_sum)
