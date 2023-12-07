#Multilevel inheritance
class Animal:
    name=''
    def eat(self):
        print("In animal")
        
class Dog(Animal):
    def eat(self):
        super().eat() #Accessing the eat function of the base class
        print("In dog")
    
    def display(self):
        print(repr(self.name))
    
d1=Dog()
d1.display()
d1.eat()

#Multilevel Inheritance
class Animal:
    def eat(self):
        print("In animal")
    
class Mammal:
    def eat(self):
        print("in mammal")
        
class Dog(Mammal, Animal):
    def eat(self):
        super().eat()
        super().eat()
        
d1=Dog()
d1.eat()