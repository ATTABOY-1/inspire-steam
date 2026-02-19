#name:triza mwaura
#date:19/02/2026
#program to show objects in python

class Human:
    #first we define the attributes of a human being
    type = "mammal"
    legs = 2
    brain = "True"
    warm_blooded = "True"
    city = "Nairobi"

    # We then create a constructor for the class object
    # The constructor will be used to create copies of class objects
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, I am {self.human_name} and here is my story:")
        print("Once upon a time, there was a human being who lived in a small village. They had many adventures and learned valuable lessons along the way. The end.")
# create the humans
amani = Human("Amani", 17)
triza = Human("Triza", 18)

# let the humans created do things
amani.tell_story()
print(f"Amani's age is {amani.human_age}")

# Modify one of the objects, without modifying other objects
triza.city = "Kiambu"

print("Triza's location is", triza.city)
print("Amani's location is", amani.city)


