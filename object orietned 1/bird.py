class Parrot:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
    
name1 = input("Insert the name of your parrot: ")
age1 = int(input("Give him his age: "))

newParrot = Parrot(name1, age1)

print(newParrot.sing("I Wonder"))
print(newParrot.dance())