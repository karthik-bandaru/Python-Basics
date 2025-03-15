class Grand_father:
    def __init__(self,g_property):
        self.g_property = g_property

    def grandpa_method(self):
        print(f"Grand_Pa property is {self.g_property}")

class Father(Grand_father):
    def __init__(self,g_property,f_property):
        super().__init__(g_property)
        self.f_property = f_property

    def father_method(self):
        print(f"Fathers Property is {self.f_property}")
        Grand_father.grandpa_method(self)

class Son(Grand_father,Father):
    def __init__(self,g_property,f_property,name):
        Grand_father.__init__(self,g_property)
        Father.__init__(self,f_property)
        self.name = name

    def son_method(self):
        print(f"My name is {self.name}")
        Father.father_method(self)

son_details = Son("Twenty lakhs","Ten lakhs","Karthi")
son_details.son_method()
      
