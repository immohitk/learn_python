"""

# Dictionary in Python

--> Dictionaries are used to store data values in key:value pairs
--> They are unordered, mutable(changeable) & don't allow duplicate keys
--> They are denoted by curly brackets {} or using the dict() function
--> Keys must be immutable, i.e., they can't be changed after creation
--> Values can be of any data type, including strings, integers, floats, lists, dictionaries, etc.
--> Dictionaries are also known as associative arrays or hash tables in other languages.

"""

info = {
    "name" : "Aman",
    "subjects" : ["python", "C", "java"],
    "topic" : ("dict", "set"),
    "age" : 20,
    "marks" : 90.5,
    "is_adult" : True
}

print(info)
print(type(info))
print(info["name"])

# ==========================================================

info["name"] = "rakesh"          # overwrite
info["surname"] = "sharma"
print(info)



# ===========================================================

null_dict = {}
print(null_dict)
print(type(null_dict))

null_dict["null"] = "dictionary"
print(null_dict)





# ===========================================================
# Nested Dictionaries
# ===========================================================


student = {
    "name" : "Rakesh",
    "score" : {
        "math" : 76,
        "science" : 85,
        "english" : 90
    },
    "age" : 20
}

print(student)
print(student["score"])
print(student["score"]["english"])


# ============================================================


# ============================================================
# Dictionary Methods
# ============================================================

myDict = {
    "name" : "Rakesh",
    "score" : {
        "math" : 76,
        "science" : 85,
        "english" : 90
    },
    "age" : 20
}

print(myDict.keys( ))               # returns all keys

print(myDict.values( ))             # returns all values

print(myDict.items( ))              # returns all (key, val) pairs as tuples

print(myDict.get( "name" ))         # #returns then key according to value

myDict.update({"city" : "Delhi"})    #inserts the specified items to the dictionary
print(myDict)
