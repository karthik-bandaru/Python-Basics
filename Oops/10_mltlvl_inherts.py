class Parent1:
    def __init__(self,f_name):
        self.f_name = f_name
    def P1(self):
        print(f"Parent 1 method {self.f_name}") 

class Parent2(Parent1):
    def __init__(self,f_name,ff_name):
        Parent1.__init__(self,f_name = "Adhi")
        self.ff_name = ff_name

    def P2(self):
        print(f"Parent 2 method {self.f_name} and {self.ff_name}")   

class Child(Parent2):
    def __init__(self,f_name,ff_name,c_name):
        Parent2.__init__(self,f_name,ff_name)
        self.c_name = c_name
    def C1(self):
        print(f"Child class {self.f_name} and {self.ff_name} and {self.c_name}")

c_inst = Child("Adhisheshayya","Rukmangadha","Karthikeya")
c_inst.C1()
c_inst.P2()
c_inst.P1()



