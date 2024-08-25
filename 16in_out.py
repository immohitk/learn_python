
# ==========================================
# File I/O in Python
# -> Python can be used to perform operations on a file. (read & write data)
# ==========================================


"""
@ Types of all files

--> 1.Text Files : .txt, .docx, .log etc.

--> 2. Binary Files : .mp4, .mov, .png, .jpeg etc.

"""

# ==========================================
# READING A FILE
# ==========================================

# f = open("demo.txt", "r")               # 'r' = open for reading (default)
# data = f.read()                         # reads entire file
# print(data)
# print(type(data))
# f.close()


# ===========================================

# f = open("demo.txt", "r")               
# data = f.read(10)                       # reads 10 characters
# print(data)
# f.close()


# ===========================================

# f = open("demo.txt", "r") 

# line1 = f.readline()                       # reads one line at a time
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


# ==========================================
# WRITING A FILE
# ==========================================



# f = open("demo.txt", "w")               # 'w' = Overwrites the entire file

# data = f.write("I want to learn JavaScript tomorrow. 1234")                        

# f.close()


# ==========================================


# f = open("demo.txt", "a")               # 'a' = adds to the file

# data = f.write("\n after that flask")                        

# f.close()



# ==========================================



# f = open("sample.txt", "x")               # 'x' = create a new file and open it for writing                      
                                                                # OR
# f.close()                                 # 'w' and 'a' can also be used for same purpose



# ==========================================



# f = open("demo.txt", "r+")               # 'r+' = open for reading and writing . The stream is positioned at the beginning of the file.
# data = f.write("abc")                       
# print(f.read())
# f.close()



# ==========================================



# f = open("demo.txt", "w+")               # 'w+' = open for reading and writing . The file is created if it doesn't exist otherwise it is truncated. The stream is positioned at the beginning of the file.
# data = f.write("abc")                       
# print(f.read())
# f.close()



# ==========================================



# f = open("demo.txt", "a+")               # 'a+' = open for reading and writing . The file is created if it doesn't exist otherwise it is truncated. The stream is positioned at the end of the file. Subsequentwrites to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.
# data = f.write("abc")                       
# print(f.read())
# f.close()




# ===========================================
# with Syntax
# ===========================================


# with open( "demo.txt","r") as f :
#     data = f.read()
#     print(data)


# with open("demo.txt", "w") as f:
#     f.write("Hello, World!")




# ===========================================
# Deleting a File
# -> using the os module
# -> Module (like a code library) is a file written by another programmer that generally has a functions we can use.
# ===========================================



# import os
# os.remove("demo.txt")