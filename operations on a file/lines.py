file = open('momo.txt', 'r')
print(file.read())
file.close()

file = open('momo.txt', 'r')
print("\n Read in parts\n")
print(file.read(192))
file.close()

file = open('momo.txt', 'a')
file.write("My nombre es Gordo")
file.close()

file = open('momo.txt', 'r')
print(file.readline(13))
file.close()