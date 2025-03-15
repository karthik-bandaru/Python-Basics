class Father:
    def __init__(self,f_name,f_age):
        self.f_name = f_name 
        self.f_age = f_age
    def father_method(self):
        print(f"My Father name is {self.f_name} and his age is {self.f_age}")

class Mother:
    def __init__(self,m_name,m_age):
        self.m_name = m_name
        self.m_age = m_age
    def mother_method(self):
        print(f"My Mother name is {self.m_name} and her age is {self.m_age}")

class Siblings:
    def __init__(self,sib_name,sib_age):
        self.sib_name = sib_name
        self.sib_age = sib_age
    def sibling_method(self):
        print(f"My sibling name is {self.sib_name} and age is {self.sib_age}")

class Son(Father,Mother,Siblings):
    def __init__(self,f_name,f_age,m_name,m_age,sib_name,sib_age,s_name,s_age):
        Father.__init__(self,f_name,f_age)
        Mother.__init__(self,m_name,m_age)
        Siblings.__init__(self,sib_name,sib_age)
        self.s_name = s_name 
        self.s_age = s_age

    def son_details(self):
        print(f"My name is {self.s_name} and i\'m {self.s_age} years old")
        print("About my family is : ")
        Father.father_method(self)
        Mother.mother_method(self) 
        Siblings.sibling_method(self)

my_name = input("Enter Ur Name : ")
my_age = int(input(f"Enter {my_name} age : "))
fa_name = input("Enter Ur Father name : ")
fa_age = int(input(f"Enter {fa_name} age : "))
ma_name = input("Enter Ur Mother name : ")
ma_age = int(input(f"Enter {ma_name} age : "))
sibs_name = input("Enter Ur sibling name : ")
sibs_age = int(input(f"Enter {sibs_name} age : "))

son_data = Son(fa_name,fa_age,ma_name,ma_age,sibs_name,sibs_age,my_name,my_age)
son_data.son_details()



