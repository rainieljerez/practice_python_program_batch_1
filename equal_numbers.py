#Prog02: Create a program that ask user to input 2 numbers.
#Print "Equal" when the numbers are the same.

print ("This program prints 'Equal' when the numbers are the same.")
#user is asked to input 2 numbers
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
#conditons then print results
if num1 == num2:
    print ("Both numbers are equal")

else:
    print ("Both numbers are not equal")