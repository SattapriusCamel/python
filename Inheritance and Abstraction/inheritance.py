class Person ( object ):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnum = idnumber
    def display(self):
        print(self.name)
        print(self.idnum)

class Employee( Person ):
    def __init__(self, name, idnumber, salary, post):
        self.pay = salary
        self.post = post
        Person.__init__(self, name, idnumber)

a = Employee('Avroot', 9101984, 192000, "Fireman")
a.display()