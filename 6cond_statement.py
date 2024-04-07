# if--elif--else (SYNTEX)

# statement should be writen after four space (python is a INDENTATION language)

"""
if(condition):
    statement1

elif(condition):
    statemenent2

else:
    statementN  

"""
#------EXAMPLE 1---------#
"""
light = input ("light colour : ")

if(light == "red"):
    print("you have to stop")
elif(light == "yellow"):
    print("you have to wait")
elif(light == "green"):
    print("you are free to go")
else:
    print("light is broken")



#------EXAMPLE 2----------#
    
marks = int(input("marks obtained : "))

if(marks >= 90):
    print("GRADE A")
elif(marks >= 80 and marks < 90):
    print("GRADE B")
elif(marks >= 50 and marks < 80):
    print("GRADE C")
else:
    print("FAILED")




#--------Single line If / Ternary Operator---------#
    

# <var> = <val1> if <condition> else <val2>
    
food = input("food :")
eat = "Yes" if food == "cake" else "No"
print(eat)


# <stt1> if <condition> else <stt2>

food = input("food :")
print("Sweet") if food == "cake" or food == "jalebi" else print("not sweet")



"""

#--------Clever If / Ternary Operator---------#


# <var> = (false_val, true_val)[<condition>]

"""
age = int(input("age :"))
vote = ("yes", "no") [age < 18]
print (vote)

"""
sal = float(input("salary :"))
tax = sal*(0.1, 0.2) [sal <= 500000]
print (tax)
