class Animal:
    def __init__(self,animal_type):
        self.animal_type = animal_type

    def animal_method(self):
        print(f"the animal Type is {self.animal_type}") 

class Dog(Animal):
    def __init__(self,animal_type,gender):
        Animal.__init__(self,animal_type)
        self.gender = gender

    def dog_method(self):
        print(f"The dog gender is {self.gender} and animal_type is {self.animal_type}")
        Animal.animal_method(self)
        

type = input("Enter what type of animal : ")
gen = input("Enter what type of gender : ")

animal_instance = Animal(type)
animal_instance.animal_method()

dog_instance = Dog(type,gen)
dog_instance.dog_method()
dog_instance.animal_method()
