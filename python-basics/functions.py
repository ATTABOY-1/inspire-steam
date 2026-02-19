#name:Alvin Njuguna
#date:18/02/2026


def cook_egg():
    oil="20ml"
    pan="true"
    moto="true"
    eggs=2
    print(f"The pan is {pan},and the fire is {moto}, add {oil} amount of oil and cook {eggs} eggs")
print("Here is statement 1")
print("Here is statement 2")
cook_egg()
print("Here is statement 3")

# Ride fare creating function
def create_fare(route,distance,is_rush_hour):
    fare =distance * 10
    if is_rush_hour==True:
        fare *= 1.5  
    print(f"The fare on{route} is {fare}")

    return fare

rush_hour=True

returned_fare=create_fare("Juja-Allsops",7, rush_hour)
print(f"The returned fare is {returned_fare}")


# Passing a list as a parameter
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interests}")

all_interests = ["bike riding","hiking", "painting", "poetry"]
write_all_interests(all_interests)