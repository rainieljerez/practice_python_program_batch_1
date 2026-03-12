#Prog07: Create a program that ask user to input 10 numbers.
#Print the sum of all the numbers.

#user is asked to input 10 numbers
number = float(input("Enter a Number: "))

#number of repetition
for i in range (9):
    number += float(input("Enter a Number: "))

print (str(number) + " is the total of the ten numbers.")