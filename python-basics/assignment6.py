# Alvin Njuguna
#Date: 17/02/2026
#Program to display a diamond pattern using asterisks

def print_diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

print_diamond(5)

def print_triangle(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
print_triangle(5)