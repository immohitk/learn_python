"""
Tuples in Python

-> A built-in data type that lets us create immutable sequences of values.
-> Tuples are defined by enclosing values in parentheses '()'.
-> Tuples are ordered collections of values that can be of any data type, including strings, integers.
-> Tuples are immutable, meaning their values cannot be modified after creation.

"""

tup = (87, 64, 33, 95, 76) 
print(type(tup))

# tup[0] = 43 -----> NOT allowed in python



tup1 = ()
print(tup1)
print(type(tup1))


tup2 = ( 1, )
print(tup2)
print(type(tup2))


tup3 = ( 1, 2, 3 )
print(tup3)
print(type(tup3))


tup4 = ( 1, 2, 3, 4 )               # tuple slicing
print(tup4[ 1 : 4])






"""
@ Tuple Methods

"""

tup5 = (2, 1, 3, 1)


tup5.index( 1 )                 # returns index of first occurrence
print(tup5.index(1))


tup5.count( 1 )                 # counts total occurrences
print(tup5.count(1))