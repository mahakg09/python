class Person:
    
    def deatils(self,name,age):
        self.name=name
        self.age=age
        print(f"the person named {self.name} is of {self.age} years")
        
    def __init__(self,lastname,classs):
        self.surname=lastname
        self.classes=classs
        print(f"{self.surname},{self.classes}")
      
obj1=Person("sharma",90)
obj1.deatils("mahak",21)

obj2=Person("garg",14) 
#When you define a method inside a class in Python, the first parameter must always be self, which refers to the instance (the object) calling the method.

class Human:
    @staticmethod
    def jankari(naaam,pata):
        print(f"jiska naam {naaam} h wo {pata} yha hai!") 
a=Human()
a.jankari("marie",233)
#What is a Static Method?
# A static method is a method that belongs to the class itself, not to any particular object.
# It does not receive self automatically.
# You must decorate it with @staticmethod.
# These methods behave like normal functions, but they sit inside a class for better organization.