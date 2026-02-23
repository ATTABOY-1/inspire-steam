#Name: Alvn Njuguna
#Date: 17/02/2026
#Program to format the output in different styles

name = "Alvin Njuguna" #name
weight = 60 # weight in kg
fav_team = "Manchester City"
height = 126.86 # height in cm

# 1.Format using print (f"{}")
print(f"My name is {name}, and I weigh {weight} kgs")

# 2. using f string
msg = f"My name is {name}, and I support {fav_team}"
print(msg)

# 3. using {} and .format()

print("My name is {0}, and I am {1} cm tall".format(name,height))

# 4. using output specifiers %s- strings %f- float

import math

print("The value of pi is approximately %.3f" % math.pi)
print("I support %s "% fav_team)
