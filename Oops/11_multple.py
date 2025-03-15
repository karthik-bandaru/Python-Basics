class Parent1:
    def __init__(self,f_name):
        self.f_name = f_name
    def P1(self):
        print(f"P1 method {self.f_name}")

class Parent2:
    def __init__(self,ff_name):
        self.ff_name = ff_name
    def P2(self):            
        print(f"P2 method {self.ff_name}")

class Child1(Parent1,Parent2):
    def __init__(self,f_name,ff_name,cc_name):
        Parent1.__init__(self,f_name)
        Parent2.__init__(self,ff_name)
        self.cc_name = cc_name
    def C1(self):
        print(f"C1 method {self.f_name} and {self.ff_name} and {self.cc_name}")

c1_inst = Child1("Adhishh","Rukkuus","Karuuu")
c1_inst.C1()
c1_inst.P1()
c1_inst.P2()