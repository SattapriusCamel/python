file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Cats')):
        print(line)
        file2.write(line)

file2.close()
file1.close()