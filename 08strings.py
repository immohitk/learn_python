
# Escape Sequence Character

"""
str1 = "This is a string. we are creating it in python"             # normal
print(str1)

str2 = "This is a string.\n we are creating it in python"           # [ \n ] escape sequence character --> next line
print(str2)

str3 = "This is a string.\t we are creating it in python"           # [ \t ] escape sequence character --> tab
print(str3)

"""


"""
String is data type that stores a sequence of characters.



--> Basic Operations

    @ concatenation
         “hello” + “world” -----> “helloworld”

    @ length of str
         len(str)

    @ Indexing
         str = “Hello_World”
         str[0] is 'H', str[1] is 'e' ...
         str[0] = 'B' #not allowed

    @ Slicing
        Accessing parts of a string

         str = “HelloWorld”
         str[ 1 : 4 ] is “ell”
         str[ : 4 ] is same as str[ 0 : 4]
         str[ 1 : ] is same as str[ 1 : len(str) ]


    @ slicing ( Negative Index )
         
         str = “Apple”
         str[ -3 : -1 ] is “pl”


"""



# --> String Functions


str = "i am a coder."

print(str.endswith("er."))         # returns true if string ends with substr

print(str.capitalize( ))           # capitalizes 1st char

print(str.replace("a", "an"))      # replaces all occurrences of old with new

print(str.find("am"))              # returns 1st index of 1st occurrence

print(str.count("am"))             # counts the occurrence of substr in string





