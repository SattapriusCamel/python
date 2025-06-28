with open('new.txt', 'w') as file:
    file.write("Hi! I Am The Linux Peinguin, & I Can Beat Windows & Mac At The Same Time")
file.close()

with open('new.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are: ")
    for line in data:
        word = line.split()
        print(word)
file.close()