import os

my_file = open("people1.txt","r")
file_data = my_file.read()
print (file_data)
my_file.close()

my_file = open("people_1.txt","a")
file_data = my_file.write(file_data)
print (file_data)
my_file.close()

os.remove("people_1.txt")
# my_file = 