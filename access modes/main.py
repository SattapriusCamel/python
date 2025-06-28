file_read = open('f.txt','r')
print(file_read.read())
file_read.close()

file_write = open('f.txt', 'w')
file_write.write("My name is Sattapriyo Kamal")
file_write.close()

file_append = open('f.txt', 'a')
file_append.write("\n I am 14 years old \n I know how to do python and JavaScript")
file_append.close()