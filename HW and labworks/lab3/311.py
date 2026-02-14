class PairAddition:

    def pair(self):
        numbers = list(map(int, input().split()))
        self.a = numbers[0]
        self.b = numbers[1]
        self.c = numbers[2]
        self.d = numbers[3]


    def sum(self):
        self.suma=self.a+self.c
        self.sumb=self.b+self.d

    def Outputres(self):
        print(f"Result: {self.suma} {self.sumb}")


a=PairAddition()
a.pair()
a.sum()
a.Outputres()            