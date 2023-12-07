#Class
'''
    1. It is a class
    2. It is an object of the object class in python. (Derived class kinda)
    3. It  is immutable object
    4. Therefore it has a hash id
'''
#Object
'''
1. Need to have self in parameter if i want to call a method using the object.
eg- class Classroom:
        def mark(self):
            print("mrked")
'''
class Classroom:
    def mark_attendance(self):
        print("ok")
    def study():
        print("studeying")
    
c=Classroom()
c.mark_attendance()
Classroom.study()
# c.stuyd() #will throw error if we di not have self object in the function. else it will only be callable by the class and not the object
Classroom.mark_attendance(c)

print(id(c))
print(hash(c))
print(type(c))


# Instance var and Class var
'''
instance:
If you write self.var then this var becomes the local variable of the object.

class:
if you define the var outside the methods. Then they become a variable accessible only through the class. 
You cannot call that variable through the object. 
If you do then that becomes another variable for the object itself. And the default value that it takes is of the class variable.
You cannot change the value of class variable inside or outside without it being local to the object or the print statement.
'''

#Constructor
'''
def __init__(self):
'''

class Student:
    global_var1=None
    global_var2=None
    def __init__(self, fname, lname, gender):
        self.fname= fname
        self.lname= lname
        self.gender= gender
        
    def hello(self):
        print("hello", self.fname)
        
    def get_gender(self):
        print(self.gender)
    
    def get_global_var(self):
        global_var1=10
        print(global_var1)
        self.global_var1=11
        print(self.global_var1)
        
s1= Student("arzoo", "bapna", "female")
s1.hello()    
s1.fname="anju"
s1.hello()
s1.fname=123
s1.hello()
s1.get_gender()
print(Student.global_var1)
# Student.get_global_var()
s1.get_global_var()
print(Student.global_var1)
print(s1.global_var1)


class Room:
    length=0.0
    breadth=0.0
    
    def cal_area(self):
        print(self.length * self.breadth)
        self.length+=1
        self.breadth+=1
        
r1=Room()
r1.cal_area()

r1.cal_area()
r1.cal_area()
r1.cal_area()

r2=Room()
r2.cal_area()

print(Room.length)
Room.length+=1
print(Room.length)

r3=Room()
r3.cal_area()
