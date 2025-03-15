class Parent:
    def __init__(self,f_name,m_name):
        self.f_name = f_name
        self.m_name = m_name

    def parntMethod(self):
        print(f"This is the parent method\nMy fath name is {self.f_name} and moth name is {self.m_name}")

class Child(Parent):
    def __init__(self,f_name,m_name,c_name):
        super().__init__(f_name,m_name)
        self.c_name = c_name

    def c_method(self):
        print(f"My name is {self.c_name}")

c_inst = Child("Rukmangadha","Padmavathi","Karthikeya")
c_inst.c_method()
c_inst.parntMethod()
