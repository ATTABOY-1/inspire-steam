#Name : Alvin Njuguna
# Date: 23/02/2026
# Program to show classes in python

class Car():
    # attributes of the car
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    # print the details of the car
    def print_details(self,model,make,color,year):
        print(f"{make} {model} of color {color} was manufactured in the {year}")
           

#instatinate a class object
my_car = Car("Atenza", "Mazda", "Red", 2022)
dads_car = Car("Land Cruiser", "Toyota", "Black", 2025)   

my_car.print_details("Atenza","Mazda","Red",2022)
dads_car.print_details("Land Cruiser","Toyota","Black",2025)



                     

