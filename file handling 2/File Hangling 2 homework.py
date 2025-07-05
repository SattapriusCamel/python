with open("txt.txt", 'r') as mickey17:
    data = mickey17.readlines()
    for line in data:
        word = line.split()
        print(word)
mickey17.close()
import os
if os.path.exists('My_File.txt'):
    print("My_file Does exist...")
    os.remove("My_File.txt")

else:
    print("My_file Does not exist-")
    My_file = open("My_File.txt", "w")
    My_file.write("Heello My Name is Sattapriyo Kamal \n Idk I Like Trains...")
    My_file.close()