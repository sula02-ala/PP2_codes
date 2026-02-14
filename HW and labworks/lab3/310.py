data = list(map(str,input().split()))

class Person:
   

    def super(self):
        self.name = data[0]
        self.gpa = float(data[1])
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

a=Person()
a.super()
a.display()



          