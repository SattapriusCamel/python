file = open('abba.txt')
print(file.read())
file.close()

filewrite = open('abba.txt', 'w')
filewrite.write("Deleting the music...")
filewrite.write("\n Uhh yeah....no music")
filewrite.close()

fileappend = open('abba.txt', 'a')
fileappend.write("\n Adding The Beatles...")
fileappend.write("\n Here comes the sun, doo, dun, doo, doo \n Here comes the sun, and I say \n It's all right")
fileappend.close()