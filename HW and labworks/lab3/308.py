numbers = list(map(int, input().split()))

class Account:
   

    def deposit(self):
        self.a = numbers[0]
    def withdraw(self):
        self.b=numbers[1]
        if self.a>=self.b:
            print(self.a-self.b)
        else:
            print("Insufficient Funds")

a=Account()
a.deposit()
a.withdraw()


          