class Parent:
    def __init__(self,father,mother):
        self.father = father
        self.mother = mother
    
    def parent_display(self):
        print(f"fathe name is {self.father} and mother name is {self.mother}")


class Child(Parent):
    def __init__(self,father,mother,name,age):
        super().__init__(father,mother)
        self.name = name
        self.age = age
        
    def display_child(self):
        print(f"child name is {self.name} son of {self.father} and age is {self.age} and his mother name is {self.mother}")
        Parent.parent_display(self)   #super().parent_display()
        
child_details = Child("rukamangadha","padma","karthik",18)

child_details.display_child()
child_details.parent_display()
# parent_details = Parent("rukamangadha","padma")
# parent_details.parent_display()