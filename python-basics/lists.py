# Alvin Njuguna
#Date: 17/02/2026
#Program to show ,ists in python
#list of friends
friends = ["Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"]

print(friends)
friends.sort() 
print(friends)

friends.reverse()
print(friends)

friends.append("Jack" )
print(friends)

new_friends = ["Tracy", "James", "Faith", "Augustine", "Don"]
print(len(new_friends))

#new list of students
students= friends + new_friends

print(students)
students.pop()
print(students)
students.insert(5,"Jenny")
print(students)
students.extend("James")
print(students)

students.remove("Joey")
print(students)
new_students= students.copy()
print(new_students)

