# Alvin Njuguna
# 2/17/2026
# program to perform arithmetic operations

f_number = 12 # first number
s_number = 34
sum_number = f_number + s_number
difference_number = f_number - s_number    
product_number = f_number * s_number
quotient_number = f_number / s_number


print("The sum of the numbers %d" % sum_number)
print("The difference of the numbers %d" % difference_number)
print("The product of the numbers %d" % product_number)
print("The quotient of the numbers %0.2f" % quotient_number)

#modulus - remainder
print(7%5)

# even and odd numbers
for x in range(0, 21):
    if (x % 2 == 1):
        print(f"{x} is an odd number")
    elif (x % 2 == 0):
        print(f"{x} is an even number")