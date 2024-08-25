
# ====================================
# OOP in Python
# -> To map with real world scenarios, we started using objects in code. This is called object oriented programming.
# -> We can create objects that have properties and methods.
# ====================================



# ====================================
# @ Class & Object in Python
# -> Class is a blueprint for creating objects.
# -> Object is an instance of a class.
# ====================================


# creating class
# class Student:
    # name ="Karan"

# creating object (instance)
# S1 = Student()
# print(S1.name)                                              # prints: Karan

# S2 = Student()
# print(S2.name)                                              # prints: Karan







# ====================================
# @ (Constructor) _ _init_ _ Function
# -> All classes have a function called __init__(), which is always executed when the object is being initiated.
# -> This function is used to assign initial values to the variables of the class.
# -> The __init__ method is a special method in Python classes. It is automatically called when an object of that class is created.
# -> It is used to set the initial state of the object.
# -> -> It is called whenever an object is created from the class and it allows the class to initialize the attributes of the class.
# ====================================


"""
----------- Note ------------- 

# :- The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# :- It does not need to be passed as a parameter when calling the method from within the class.

"""

# ====================================
# Class & Instance Attributes
# -> Class.attr
# -> obj.attr
# ====================================


"""
class Student:                                      #|-----> Class Attribute
   
   # Default constructors
   def __init__(self):
     pass

   # Prameterized constructors
   def __init__(self, fullname, marks):
    self.name = fullname                            #|-----> Instance or Object Attribute
    self.marks = marks                              #|-----> Instance or Object Attribute
    print("adding new student in database..")



S1 = Student("Karan", 92)
print(S1.name)                          # prints: Karan   
print(S1.marks)                         # prints: 92

S2 = Student("Ravi", 85)
print(S2.name)                          # prints: Ravi
print(S2.marks)                         # prints: 85

S3 = Student("Aryan", 72)
print(S3.name, S3.marks)                # prints: Aryan 72               

"""





# ====================================
# Methods
# -> Methods are functions that belong to objects.
# -> Methods are used to perform some specific task.
# -> Methods are defined inside a class.
# ====================================



"""

class Student:        

    college_name = "ABC college"                              
   
    def __init__(self, fullname, marks):
        self.name = fullname                            
        self.marks = marks 
    
    def welcome(self):
      print("Welcome Students", self.name)    

    def get_marks(self):
       return(self.marks)
                         


S1 = Student("Karan", 92)
S1.welcome()
print(S1.get_marks())


"""





# ====================================
# Static Methods
# -> Methods that don’t use the self parameter (work at class level).
# -> Static methods are used to perform some specific task.
# -> Static methods are defined inside a class using the @staticmethod decorator.
# ====================================




"""
----------- Decorators ------------- 

:- Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
:- Decorators are often used for logging, authentication, authorization, rate limiting, caching, and validation of user input.
:- A decorator is a small function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
:- The @ symbol before a function name is a decorator, it is used to call the decorator function and pass the function to be decorated as an argument to the decorator function.
:- The decorator function returns a new function that "wraps" the original function. The new function produced by the decorator is then called instead of the original function when it is invoked.
:- The decorator function can perform any operation before calling the original function and can also access the return value of the original function.
:- The decorator function can also modify the original function in some way, such as by adding a new method to the function object.

"""



"""

class Student:        

    def __init__(self, fullname, marks):
        self.name = fullname                            
        self.marks = marks 

    @staticmethod                               # Decorator
    def college( ):
        print( "ABC College" )

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg marks is", sum/3)


S1 = Student("Karan", [92, 83, 74])
S1.get_avg()
S1.college()

S1.name = "John"
S1.marks = [54, 36, 78]
S1.get_avg()


"""