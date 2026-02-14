import math

class CircleArea:

    def takeRadius(self):
        self.a=int(input())

    def area(self):
        print(round((self.a**2)*math.pi,2))


a=CircleArea()
a.takeRadius()
a.area()            