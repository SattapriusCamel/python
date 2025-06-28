new_file = open('open_File.txt', 'x')
new_file.close()


import os
print("Checking if the new file exist...\n")
if os.path.exists('my_new_file.txt'):
    print("Exists!")
    os.remove('my_new_file.txt')
else:
    print("Does NOT exist...")
mynewfile = open('my_new_file.txt', 'w')
mynewfile.write("Linux Peinguin SOLOS Windows")
mynewfile.close()
os.remove('open_File.txt')
os.rmdir('new stuff')