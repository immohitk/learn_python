# ===============================================

# ----------- Important ------------- 

# :- 1. Abstraction - Hiding the implementation details of a class and only showing the essential features to the user.
# :- 2. Encapsulation - Wrapping data and functions into a single unit (object).
# :- 3. Inheritance - Creating a new class from an existing class.
# :- 4. Polymorphism - The ability of an object to take on multiple forms.

# ===============================================




"""

1. Abstraction

:- Abstraction is a fundamental concept in object-oriented programming (OOP) that helps to hide the implementation details of an object from the outside world, showing only the essential features to the user.
:- It is a way to show only the necessary information to the outside world while hiding the internal details of an object.
:- Abstraction is achieved through abstraction classes or interfaces.
:- Abstraction classes are classes that have abstract methods, which are methods that are declared but not defined in the class. These methods must be implemented by any class that inherits from the abstraction class.
:- Abstraction interfaces are interfaces that have abstract methods, which are methods that are declared but not defined in the interface. These methods must be implemented by any class that implements the abstraction interface.
:- Abstraction is useful when you want to show a simplified view of a complex system to the outside world.

"""




"""

2. Encapsulation

:- Encapsulation is a fundamental concept in object-oriented programming (OOP) that binds together the data and the methods that manipulate that data, and keeps both safe from external interference and misuse.
:- It is a way to hide the internal state of an object from the outside world, and only expose the necessary information through public methods.
:- Encapsulation is achieved through encapsulation classes or objects.
:- Encapsulation classes are classes that have private data members, which are data members that are accessed through public methods.
:- Encapsulation objects are objects that have private data members, which are data members that are accessed through public methods.
:- Encapsulation is useful when you want to protect the internal state of an object from external interference.
:- It helps to prevent data corruption and ensures data integrity.
:- It also helps to improve code reusability and maintainability.


"""





# Example 1 :-

"""

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started..")

car1 = car()
car1.start()

"""




# ========================================
# del keyword
# -> del keyword is used to delete an object property or an object itself.
# ========================================


"""

# Example 2 :-

class student:
    def __init__(self, name):
        self.name = name

s1 = student("Aman")
print(s1.name)
del s1
print(s1.name)  


"""


# ========================================
# private(like) attributes & methods

# @ conceptual implementations in python
# -> private attributes and methods are meant to be used only within the class and are not accessible from outside the class
# ========================================



# Example 3 :-

"""

class account:
    def __init__(self, acc_no, acc_pass):
        self.account_no = acc_no
        self.__account_password = acc_pass      # private attribute

    def reset_pass(self):
        print(self.__account_password)      # private method

acc1 = account("12345", "qwerty")

print(acc1.account_no)  
print(acc1.reset_pass())  


"""


# Example 4 :-

"""

class person:
    __name = "Ravi"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())

    
"""






"""

3. Inheritance

:- It is a mechanism in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class.
:- The class that is being inherited is called the parent class or superclass.
:- The class that is doing the inheriting is called the child class or subclass.
:- Inheritance allows for code reusability and helps to promote the "is-a" relationship between classes.
:- There are four types of inheritance: single inheritance, multiple inheritance, multilevel inheritance, and hierarchical inheritance.
:- Inheritance is useful when you want to create a new class that is a modified version of ancexisting class.
:- It helps to reduce code duplication and improve code maintainability.
:- It also helps to promote the "is-a" relationship between classes.
:- It is useful when you want to create a class that is a specialization of an existing class.
:- It helps to improve code reusability and maintainability.
:- It also helps to improve code readability and understandability.
:- It is useful when you want to create a class that is a combination of multiple existing classes.


"""





# =======================================
# @ Inheritance type
# =======================================
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance
# =======================================




# Example 5 :-  Single Inheritance

"""
class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")



class Toyota_car(car):
    def __init__(self, name):
        self.name = name

car1 = Toyota_car("fortuner")
car2 = Toyota_car("prius")

print(car1.start())

"""







# Example 6 :-  Multilevel Inheritance

"""

class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")



class Toyota_car(car):
    def __init__(self, brand):
        self.brand = brand


class fortuner(Toyota_car):
    def __init__(self, type):
        self.type = type
        
car1 = fortuner("diesel")
print(car1.start())


"""






# Example 7 :-  Multilple Inheritance

"""

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varA)
print(c1.varB)

"""






# ================================================
# Super Method
# -> super() method is used to access methods of the parent class.
# ================================================



# Example 8 :-


"""

class car:

    def ___init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")



class Toyota_car(car):
    def __init__(self, name, type):
        super().___init__(type)
        self.name = name
        super().start()
        

car1 = Toyota_car("diesel", "electric")
print(car1.type)

"""







# ================================================
# Class Method
# -> A class method is bound to the class & receives the class as an implicit first argument.

# Note :- static method can't access or modify class state & generally for utility.
# ================================================




# Example 9 :-

"""

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = "Rahul"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

"""





# ================================================
# Property(decorator)
# -> We use @Property decorator on any method in the class to use the method as  a property.
# ================================================



# Example 10 :-

"""

class student:
    
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math 


    # def calPercentage(self):
    #      self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)

"""









"""

4. Polymorphism

:- Polymorphism is the ability of an object to take on multiple forms.
:- It is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass.
:- Polymorphism is achieved through method overriding or method overloading.
:- Method overriding is a technique where a subclass provides a different implementation of a method that is already defined in its superclass.
:- Method overloading is a technique where multiple methods with the same name can be defined, but with different parameters.
:- Polymorphism is useful when you want to write code that can work with objects of different classes
:- It helps to improve code reusability and maintainability.
:- It also helps to improve code readability and understandability.
:- It is useful when you want to create a class that can work with objects of different classes.

"""


# ============================================
# Polymorphism : Opertor Overloading

#-> when the same operator is allowed to have different meaning according to the context.
# ============================================


"""
-> Opertors & Dunder functions

a+b  # addition                 a__add__(b)

a-b  # substraction             a__sub__(b)

a*b  # multiplication           a__mul__(b)

a/b  # divison                  a__truediv__(b)

a%b  # modulo                   a__mod__(b)

"""





# Example 11 :- complex number

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal, newImg)
    
    def __mul__(self, num2):
        newReal = self.real * num2.real
        newImg = self.img * num2.img
        return complex(newReal, newImg)
    
    def __truediv__(self, num2):
        newReal = self.real / num2.real
        newImg = self.img / num2.img
        return complex(newReal, newImg)
    
    def __mod__(self, num2):
        newReal = self.real % num2.real
        newImg = self.img % num2.img
        return complex(newReal, newImg)
    
    

num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4, 6)
num2.showNumber()

num3 = num1 + num2              # addition
num3.showNumber()

num4 = num1 - num2              # substraction
num4.showNumber()

num5 = num1 * num2              # multiplication
num5.showNumber()

num6 = num1 / num2              # division
num6.showNumber()

num7 = num1 % num2              # modulo
num7.showNumber()