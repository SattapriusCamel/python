file = open('abba.txt', "r")
counter = 0
content = file.read()
colist = content.split("\n")
for i in colist:
    if i:
        counter += 1
print("This is the number of lines: ")
print(counter)