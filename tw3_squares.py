'''
TW3: Odometer - Low_high number
Write a program that asks the user for a low integer and a
high integer and then uses a while-loop to print out all the integers from low to high.
If the user types in the low and high bounds in the wrong order, automatically reverse them.
Only print out the integers in the given range that are perfect squares (1, 4, 9, etc.).
Authors: Melinda Davis
ChangeLog (Who,When,What):
MDavis, 10-03-2022, Created Script
'''

# Get user input
low_num = int(input("low: "))
high_num = int(input("high: "))

# Program automatically reverses numbers if user inputs them incorectly
if low_num > high_num:
    (low_num, high_num) = (high_num, low_num)

# While loop to iterate through the numbers and print them out
while low_num <= high_num:
    print(low_num)
    low_num += 1

input("Please hit enter to quit the program.")
