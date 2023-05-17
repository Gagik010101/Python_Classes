class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        print(f"Rectengle perimeter = {2*(self.length + self.width)}sm")
    def Area(self):
        print(f"Rectengle area = {self.length * self.width}sm^2")

class Parallelepipede(Rectangle):
     def __init__(self, length, width, height):
         Rectangle.__init__(self, length, width)
         self.height = height

     def Volume(self):
         print(f"Volume parallelepipede = {self.length * self.width * self.width} cm^3")

n = input("input 1 for Perimeter\ninput 2 for Area\ninput 3 for Voliume\n")

length = int(input("input lenght:\t"))
width = int(input("input widht:\t"))
if n == "1":
    P = Rectangle(length, width)
    P.Perimeter()
elif n == "2":
    A = Rectangle(length, width)
    A.Area()
elif n == "3":
    highte = int(input("input height:\t"))
    A = Parallelepipede(length, width, highte)
    A.Volume()
else:
    print('Error')
