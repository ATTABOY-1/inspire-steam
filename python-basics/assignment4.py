#Name: Alvin Njuguna
#Date: 13/02/2026
#Program to calculate geometric progression

# Calculating nth term of a geometric progression

a = int(input("Enter the first number:"))
n = int(input("Enter number of terms:"))
r = int(input("Enter the common ratio:"))

nth_term = a*(r**(n-1))
sn = a*(r**n - 1)/(r-1)

print(f"The sum of the numbers is: {sn}")
print(f"The nth term is: {nth_term}")