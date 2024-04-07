#---- EXPRESSION EXECUTION ----#

# 1--> ( string & numeric values can operate together with ' * ')

A = 2
B = 3

Txt = "@"

print(2*Txt*3)



# 2--> ( String and string can operate with ' + ') (also known as concatination)

C = "2"
D = 3

Nit = "@"

print((C+Nit)*D)



# 3--> ( Numeric value can operate with all arithematic operators ) (+,-,*,..etc)

E = 2
F = 3
G = 4

print(E+F*G)




# 4--> ( Arithemetic expression with interger and float gives float)

H = 10
I = 5.0

J = H*I

print(J)




# 5--> ( Result of division operator with two integer will be float )

K = 2
L = 3

M = K/L

print(M)





# 6--> ( Integer division by float and int will give int displayed as float )

N = 5.0
O = 10

P = N//O            # give closest lower digit

print(P, N/O)




# 7--> ( remainder is negative when denominator is negative )

a = -5        # numertor
b = 2         # denominator
c = a%b 

print(c)      # output = remender




d = 5         # numertor
e = 2         # denominator
f = d%e

print(f)      # output = remender




g = 5         # numertor
h = -2        # denominator
i = g%h

print(i)      # output = remender




j = -5        # numertor
k = -2        # denominator
l = j%k

print(l)      # output = remender