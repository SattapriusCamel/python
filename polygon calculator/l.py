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

print("Select Shape" \
"1 - Triangle" \
"2 - Square" \
"3 - Pentagon" \
"4 - Hexagon")
shapechoice = int(input("Insert Number: "))

if shapechoice == 1:
    lengthofside = int(input("Set the side length of your triangle: "))
    newtri = triangle(lengthofside)
    print("The perimeter of the triangle is: ")
    print(newtri.findpermeter())
if shapechoice == 2:
    lengthofside = int(input("Set the side length of your square: "))
    newtri = sqaure(lengthofside)
    print("The perimeter of the sqaure is: ")
    print(newtri.findpermeter())
if shapechoice == 3:
    lengthofside = int(input("Set the side length of your pentagon: "))
    newtri = pentagon(lengthofside)
    print("The perimeter of the pentagon is: ")
    print(newtri.findpermeter())
if shapechoice == 4:
    lengthofside = int(input("Set the side length of your hexagon: "))
    newtri = hexagon(lengthofside)
    print("The perimeter of the hexagon is: ")
    print(newtri.findpermeter())
