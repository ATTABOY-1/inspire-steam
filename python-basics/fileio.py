#Name : Alvin NJuguna
# Date : 24/02/2026
# Program to show file handling in python


#create new file 
import os


new_file = open("newfile.txt", "r+")

#write to new file
new_file.write("student name: alvin njuguna ,ID:22202666 , email:alvinnjuguna28@gmail.com,course:law ")
new_file.close()


#read from file
new_file = open("newfile.txt", "r")
data=new_file.read()
print(data)
new_file.close()

#delete file
#import os
os.remove("remove.txt")




#delete folder