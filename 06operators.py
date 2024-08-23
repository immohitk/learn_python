'''
An operator is a symbol that performs a certain operation between operands.


Arithmetic Operators ( + , - , *, / , % ,** )
====================================================================
Relational / Comparison Operators ( == , != , > , < , >= , <= )
====================================================================
Assignment Operators ( = , +=, -= , *= , /= , %= , **= )
====================================================================
Logical Operators ( not , and , or )


'''


'''
Note :- == to check the equality
     :- != means not equal to

'''


# ====================================================================
# Arithmetic Operators
# ====================================================================


a = 100
b = 50

sum = a + b
diff = a - b
multi = a * b
divi = a / b
remen = a % b
powe = a ** b 


print(sum)
print(diff)
print(multi)
print(divi)
print(remen)
print(powe)



# ====================================================================
# Relational / Comparison Operators
# ====================================================================


c = 100
d = 50
 
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)




# ====================================================================
# Assignment Operators
# ====================================================================


num = 10
num = num + 10

print("num : ", num)

# num += 10   and  num = num + 10 are same       
# num -= 10   and  num = num - 10 are same  
# num *= 10   and  num = num * 10 are same
# num /= 10   and  num = num / 10 are same
# num %= 10   and  num = num % 10 are same
# num **= 10   and  num = num ** 10 are same     

 

# ====================================================================
# Logical Operators
# ====================================================================


val1 = True
val2 = False
 
print("AND operator =", val1 and val2)
print("OR operator =", val1 or val2)
print("NOT operator of val1 =", not val1)
print("NOT operator of val2 =", not val2)


