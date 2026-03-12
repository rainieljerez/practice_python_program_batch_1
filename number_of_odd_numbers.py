#Prog08: Create a program that ask user to input 10 numbers.
#Print how many are odd numbers.
odd = 0
#user is asked to input 10 numbers
for i in range (10):
    num = float(input("Enter a Number: "))
    if num % 2 != 0:
        odd += 1

print (odd, "is the total of odd numbers")


