#Prog05: Create a program that ask user to input 2 numbers.
#Print the quotient of the two numbers with the decimal point

print ("This program prints the quotient of two numbers.")
#user is asked to input 2 numbers
num1 = float(input("Enter Dividend: "))
num2 = float(input("Enter Divisor: "))

if num2 > num1:
    print("Cannot be")

elif num1 / num2:
    quotient = num1 / num2
    print("The quotient of the two numbers " + str(quotient))



