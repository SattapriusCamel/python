outputfile = open('ouptut.txt', 'w')
inputfile = open('new.txt', 'r')
lines_seen_so_far = set()
print("Eliminating Copied Lines")
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add
inputfile.close()
outputfile.close()

