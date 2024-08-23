"""
# Set in Python

--> Set is the collection of the unordered items.
--> Each element in the set must be unique & immutable.
--> It is a mutable data type in Python.
--> It is defined by using the curly brackets {} or set() function.
--> It is used to store the collection of the unique items.
--> It is used to remove the duplicate values from the list.
--> It is used to perform the mathematical operations like union, intersection, difference etc.
--> It is used to perform the set operations like symmetric difference, subset, superset etc.

"""


collection = { 1, 2, 3, 4, "hello", "world", 2, 2, "world"}

print(collection)
print(type(collection))
print(len(collection))


collection2 = set()           # empty set
print(collection2)



# ===========================================
# Set Methods
# ===========================================


collection3 = set()              # empty set


collection3.add(1)               #adds an element
collection3.add(2)
collection3.add(3)
collection3.add(4)


# collection3.remove(3)            #removes the elem an

# collection3.clear( )             #empties the set

print(collection3.pop())           #removes a random value


print(collection3)

# ===========================================

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union( set2 ))                   # combines both set values & returns new

print(set1.intersection( set2 ))            # combines common values & returns new

print(set1.difference( set2 ))              # difference betwwen set1 and set2
print(set2.difference( set1 )) 