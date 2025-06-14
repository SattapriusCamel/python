class Person ( object ):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def display(self):
        print(self.firstname)
        print(self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.graduationyear = year

x = Student("Dropout", "Bear", 2007)
x.display()
print(x.graduationyear)