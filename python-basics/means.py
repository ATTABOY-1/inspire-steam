#Name: Alvin Njuguna
#Date: 16/02/2026
#Program to calculate means of numbers

sum=0
for x in range (0,100,2):
    new_sum=sum+x
    sum=new_sum
print(f"Sum of numbers from 0 to 99 is {sum}")
mean=sum/50
print(f"Mean of numbers from 0 to 99 is {mean}")


print(3%2) # modulus operator gives the remainder of division