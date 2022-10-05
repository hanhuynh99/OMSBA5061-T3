'''
TW3: Odometer
Write a program that emulates a 4-digit odometer. It prints out from 0 0 0 . 0 to 9 9 9 . 9.
Authors: Melinda Davis
ChangeLog (Who,When,What):
MDavis, 10-03-2022, Created Script
Utilized Figure 4.8.1 Nested loop from zybook as guide for this code
'''

# Declare Variables
pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0

# Utilize while loop to iterate through values. Print statement prints odometer one by one
while pos1 <= 9:
    pos2 = 0
    while pos2 <= 9:
        pos3 = 0
        while pos3 <= 9:
            pos4 = 0
            while pos4 <= 9:
                print(pos1, pos2, pos3, ".", pos4)
                pos4 = pos4 + 1
            pos3 = pos3 + 1
        pos2 = pos2 + 1
    pos1 = pos1 + 1

input("Please hit enter to quit the program.")
