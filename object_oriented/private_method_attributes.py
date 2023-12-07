class Class1:
    def __init__(self):
        self.__maxPrice=900
    
    def setPrice(self, price):
        self.__maxPrice=price
        
    def display(self):
        print(self.__maxPrice)
        
    def __privMethod(self):
        print("In priv method")
        
c1=Class1()
c1.display()
c1.setPrice(2000)
c1.display()
c1.__maxPrice=1000
print(c1.__maxPrice)
# c1.__privMethod() #cannot access private methods

class Class2(Class1):
    def display(self):
        # print(self.__maxPrice) #cannot access the private members of the sueperclass
        pass
        
c2=Class2()
c2.display()