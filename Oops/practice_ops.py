class Age:
    def __init__(self,dob):
        self.dob = dob

    def age(self):
        print("Your age is ",2024-self.dob)

instance = Age(2006)
instance.age()

class Parent:
    def __init__(self,f_name = "nanna"):
        self.f_name = f_name

    def pfn(self):
        print(f"My father name is {self.f_name}")
class Child(Parent):
    def __init__(self,f_name,c_name):
        Parent.__init__(self,f_name="Rukmangadha")
        self.c_name = c_name
    def fn(self):
        print(f"My name is {self.c_name} and my pappa name is {self.f_name}")

inst = Child("Rukku","karthi")
inst.fn()
inst.pfn()
