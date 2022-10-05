'''
TW3: Odometer - Low_high number
Write a program that asks the user for a low integer and a
high integer and then uses a while-loop to print out all the integers from low to high.
Authors: Melinda Davis
ChangeLog (Who,When,What):
MDavis, 10-03-2022, Created Script
'''

# Get user input
low_num = int(input("low: "))
high_num = int(input("high: "))

# While loop to iterate through the numbers and print them out
while low_num <= high_num:
    print(low_num)
    low_num += 1

input("Please hit enter to quit the program.")
