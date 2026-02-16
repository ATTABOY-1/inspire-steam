#Name : Alvin Njuguna
# Date : 11/02/2026
# Program to calculate factorial of numbers

factorial=1 #initialize factorial to 1
number=int(input("Enter the number x:"))
for x in range (1,number+1):
    factorial*=x
    

    print(f"{number}! = {factorial}")

