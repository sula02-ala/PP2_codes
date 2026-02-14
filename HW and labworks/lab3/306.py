class Shape:

    def getLength(self):
        numbers = list(map(int, input().split()))
        self.a = numbers[0]
        self.b = numbers[1]


    def Classdeterminant(self):
        if self.a == self.b:
            self.shape = "Square"
        else:
            self.shape = "Rectangle"

    def Area(self):
        if self.shape == "Square":
            print(self.a * self.a)
        else:
            print(self.a * self.b)


a = Shape()
a.getLength()
a.Classdeterminant()
a.Area()
