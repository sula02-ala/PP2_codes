import math

class PointCoordinates:
    def getcoordinates(self):
        numbers = list(map(int, input().split()))
        self.a = numbers[0]
        self.b = numbers[1]

    def move(self):
        num = list(map(int, input().split()))
        self.newa = num[0]
        self.newb = num[1]

    def secondpoint(self):
        numb = list(map(int, input().split()))
        self.c = numb[0]
        self.d = numb[1]    

    def show(self):
        print(f"({self.a}, {self.b})")

    def shownew(self):
        print(f"({self.newa}, {self.newb})")

    def dist(self):
        return (((self.c-self.newa)**2 + (self.d-self.newb)**2)**0.5)

a=PointCoordinates()
a.getcoordinates()
a.move()
a.secondpoint()
a.show()
a.shownew()
print(f"{a.dist():.2f}")