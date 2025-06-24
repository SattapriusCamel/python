class triangle:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 3
class sqaure:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 4
class pentagon:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 5
class hexagon:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 6
class heptagon:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 7
class octogon:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 8
class nonagon:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 9
class decagon:
    def __init__(self, sidelength):
        self.sidelength = sidelength
    def findpermeter(self):
        return self.sidelength * 10

print("Select Shape \n 1 - Triangle \n 2 - Square \n 3 - Pentagon \n 4 - Hexagon \n 5 - Heptagon \n 6 - Octogon \n 7 - Nonagon \n 8 - Decagon")
shapechoice = int(input("Insert Number: "))

if shapechoice == 1:
    lengthofside = int(input("Set the side length of your triangle: "))
    newtri = triangle(lengthofside)
    print("The perimeter of the triangle is: ")
    print(newtri.findpermeter())
elif shapechoice == 2:
    lengthofside = int(input("Set the side length of your square: "))
    newtri = sqaure(lengthofside)
    print("The perimeter of the sqaure is: ")
    print(newtri.findpermeter())
elif shapechoice == 3:
    lengthofside = int(input("Set the side length of your pentagon: "))
    newtri = pentagon(lengthofside)
    print("The perimeter of the pentagon is: ")
    print(newtri.findpermeter())
elif shapechoice == 4:
    lengthofside = int(input("Set the side length of your hexagon: "))
    newtri = hexagon(lengthofside)
    print("The perimeter of the hexagon is: ")
    print(newtri.findpermeter())
elif shapechoice == 5:
    lengthofside = int(input("Set the side length of your heptagon: "))
    newtri = heptagon(lengthofside)
    print("The perimeter of the heptagon is: ")
    print(newtri.findpermeter())
elif shapechoice == 6:
    lengthofside = int(input("Set the side length of your octogon: "))
    newtri = octogon(lengthofside)
    print("The perimeter of the octogon is: ")
    print(newtri.findpermeter())
elif shapechoice == 7:
    lengthofside = int(input("Set the side length of your nonagon: "))
    newtri = nonagon(lengthofside)
    print("The perimeter of the nonagon is: ")
    print(newtri.findpermeter())
elif shapechoice == 8:
    lengthofside = int(input("Set the side length of your decagon: "))
    newtri = decagon(lengthofside)
    print("The perimeter of the decagon is: ")
    print(newtri.findpermeter())
else:
    print("Invalid number")

