class Parent:
    def __init__(self,fath,moth):
        self.fath = fath
        self.moth = moth
    def display(self):
        print(f"Father name is {self.fath} and mother name is {self.moth}")

class Child(Parent):
    def __init__(self,fath,moth,son1,son2):
        super().__init__(fath,moth)

        self.son1 = son1
        self.son2 = son2
    def display(self):

        print(f"son1 = {self.son1} and son2 = {self.son2} and their fath name is {self.fath} and moth is {self.moth}")

        super().display()

# parent_details = Parent("Ruk","Pad")
# parent_details.display()

child_details = Child("ruk","pad","kar","moha")
child_details.display()

