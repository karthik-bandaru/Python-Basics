class Nobitha:
    def __init__(self,name,age):
        self.n = name
        self.a = age
    def display(self):
        print(f"My name is {self.n} and im {self.a} years old")

# name = input("Enter Ur name: ")
# age = int(input("Enter Ur age: "))

my_details = Nobitha(input("Enter ur name"),int(input("ENter ur age")))
my_details.display()

class Table:
    def table(self,num):
    
        for i in range(1,11):
            print("{} * {} = {}".format(num,i,num*i))
num = int(input("Enter which table u want : "))
t = Table()
t.table(num)