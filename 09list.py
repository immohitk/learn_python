
"""
# Lists in Python

--> A built-in data type that stores set of values

--> It can store elements of different types (integer, float, string, etc.)

"""


#1

marks = [87, 64, 33, 95, 76]
print(marks)
print(marks[0])
print(marks[3])



#2

student = ["Karan", 85, "Delhi"]
print(student)

student[0] = "Arjun"                    #allowed in python
print(student)

print(len(student))                     #returns length



# Note :- Strings are immutable in python means it cannot be changed whereas List is mutable in python means it can be changed.






"""
@ List Slicing

        -> Similar to String Slicing

        -> list_name[ starting_idx : ending_idx ]          # ending idx is not included

"""


#3

marks1 = [87, 64, 33, 95, 76]

print(marks1[1:4])

print(marks1[ : 4 ])         # is same as marks[ 0 : 4]

print(marks1[ 1 : ])         # is same as marks[ 1 : len(marks) ]

print(marks1[ -3 : -1 ])             # is [33, 95]





"""
@ List Methods

"""


#4

list = [2, 1, 3]


list.append(4)                # adds one element at the end
print(list)                   # [2, 1, 3, 4]


list.sort( )                  # sorts in ascending order
print(list)                   # [1, 2, 3, 4]


list.sort( reverse=True )     # sorts in descending order
print(list)                   # [4, 3, 2, 1]


list.reverse( )               # reverses list
print(list)                   # [1, 2, 3, 4]


list.insert( 2, 5 )           # insert element at index
print(list)                   # [1, 2, 5, 3, 4]


list.remove(1)                # removes first occurrence of element
print(list)                   # [2, 5, 3, 4]


list.pop(3)                   # removes element at idx
print(list)                   # [2, 5, 3]