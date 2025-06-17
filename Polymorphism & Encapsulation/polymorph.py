class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old")
    def make_sound(self):
        print("Bark")

namecat = input("Name Your Cat: ")
namedog = input("Name your Dog: ")
agecat = int(input("Set the age of your cat: "))
agedog = int(input("Set the age of your dog: "))

cat1 = Cat(namecat,agecat)
dog1 = Dog(namedog, agedog)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()

