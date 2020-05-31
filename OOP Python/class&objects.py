
#TODO
''' OBJECT , CLASS , ENCAPTULATION , INHERITANCE 
    ABSTRACTION , POLYMORPHOSIM '''
#? what is object ?
'''
object is also called as instance
attribute + behaviour = object
attribute ex :- age , name , height (value/variable)
behaviour ex :- wlking , eating (function)
in oop behaviour/function is called method
'''
#? what is class ?
''' blueprint for creating objects 
    in a class we can design an object

    class name :
        arrribute : behaviour
'''

class MyComputer: #! create a class

  def config(self): #! create a blueprint for instance
      print("i5,16gb,1tb")

comp1 = MyComputer() #! create an object
# print(type(comp1))    
MyComputer.config(comp1) #! call object 1
comp1.config() #! call object 2

#? special method __init__

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("processor",cpu,ram) # no need to call the method init automatically call when we create object
    def config(self):
        print("config is",self.cpu,self.ram)


com = Computer('i5',16) # here we pass 3 arg 1 is the object itself cpu & rams
com.config()

#? CONSTRUCTOR 
#! constructor deside how much memory require your variable in heap memeory

#? VARIABLES IN OOP PYTHON

'''
instance variable
class / static variable 
'''
class car:
    wheels = 4 # Global variable or class variable
    def __init__(self): # self is like a pointer
        self.company = "bmw"
        self.milage = 10

c1 = car()
c2 = car()
c1.company = "audi"
print(c1.company,c1.wheels)
print(c2.company,c2.wheels)

#?  Decorator 
'''
decorator is used for class variable
'''
class Student:
    school = "sjinstitute"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod   
    def getschool(cls):
        return cls.school 

s1 = Student(20,25,30)
s2 = Student(30,35,30)
print(s1.avg())
print(s2.avg())
print(Student.getschool())

#TODO
'''
Getter , Setter 

'''