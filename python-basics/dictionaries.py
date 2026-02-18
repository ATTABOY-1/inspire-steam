# Alvin Njuguna
#Date: 17/02/2026
#Program to show dictionaries in python

car = {"Model" : "Audi", 
        "make" : "Q8",
       "Color" : "cherry",
        "Year" : 2025}
print(car)

print(car["Model"])
print(car["Year"])

students=dict({"Alice": 18,
               "James": 22,
               "Mark": 20,
               "Daisy": 19})

for key in students:
    print(key)
for val in students.values():
    print(val)
