"""
@ Loops in Python

"""
# ==================================================
#  while Loops
# ==================================================


"""
count = 1               # (count) variable is called Iterator.

while count <=5 :       # this process of loop is called Iteration.
    print("hello", count)
    count += 1

print(count)

"""

# ===================================================

"""
i = 5

while i >= 1 :
    print(i)
    i -= 1

"""







# =====================================================
# Break & Continue
# =====================================================

"""
Break : used to terminate the loop when encountered

Continue : used to skip the current iteration when encountered

"""

# BREAK

"""
b = 1

while b <= 10 :
    print(b)
    if (b == 5) :
        break
    b += 1

"""

# CONTINUE

"""
c = 1

while c <= 10 :
    if (c%2 != 0) :
        c += 1
        continue
    print(c)
    c += 1

"""








# =========================================================

# For Loop

# -> Loops are used used for sequential traversal. For traversing list, string, tuples etc.
# -> It is used for iterating over a sequence (such as a list, tuple, dictionary, set, etc.) or other iterable object, like files or streams.

# =========================================================


# @ for Loop

# for el in list:


# nums = [1, 2, 3]

# for val in nums:
#     print(val)



# @ for Loop with else

"""
nums2 = [1, 2, 3, 4, 5]

for val in nums2 :
    if (val == 3) :
        print("3 foumd")
        break
    print(val) 
else:
    print("No items in list")

"""







# =============================================

# range( )


# -> range() is a built-in Python function that generates a sequence of numbers starting from the first argument up to, but not including, the second argument. It is used to generate a sequence of numbers for a loop.

# -> It is used to generate a sequence of numbers for a loop.

# range( start?, stop, step?)

# =============================================


# seq = range(10)

# for i in seq :
#     print(i)


#   OR


# for i in range(10):          # range(stop)
#     print(i)


# =============================================

# for j in range(2, 10):       # range(start, stop)
#     print(j)


# =============================================

# for k in range(2, 10, 2):       # range(start, stop, step)
#     print(k)









# =============================================
# Pass Statement

# -> pass is a null statement that does nothing. It is used as a placeholder for future code.
# =============================================



for el in range(0):
    pass