#Name : Alvin Njuguna
# Date : 11/02/2026
# Program to calculate income tax

salary = int(input("Enter your gloss salary: "))

if salary < 50000 :
    tax = (2.5 * salary) / 100
    net_salary = salary - tax
    print(f"Gross salary = {salary}")
    print(f"net_salary = {net_salary}")
    print(f"tax = {tax}")
elif salary >= 50000 and salary <= 100000 :
    tax = (4.5 * salary) / 100
    net_salary = salary - tax
    print(f"Gross salary = {salary}")
    print(f"net_salary = {net_salary}") 
    print(f"tax = {tax}")
elif salary > 100000 :
    tax = (7.5 * salary) / 100
    net_salary = salary - tax    
    print(f"Gross salary = {salary}")
    print(f"net_salary = {net_salary}") 
    print(f"tax = {tax}")

