# #int type
# a = 5
# print(f"the value of a is:{a} and of {type(a)}")
# #float type
# f1 = 10.5
# print(f"the value of f1 is : {f1} and the type is of {type(f1)}")
# #string type
# b = "Moni"
# print(b)
# print(type(b))
#---------------------------------------------------------------------------
str1 = "Hello"
str2 = "Swapnadip"
s = "python123"
#accessing elements of a string by indexes
# print(str1[2])
# print(str2[-1])
#slicing a string
print(str1[1:4]) #Start index 1, end index 4
print(str2[2:]) #Start index 2, end index is the end of the string
print(str2[:5]) #start index is 0, end index is 5
print(str2[::-1]) #reverse the string

#string methods
print(s.upper())   # HELLO WORLD
print(s.lower())   # hello world
print(s.title())   # Hello World (Capitalizes each word)
print(s.capitalize())  # Hello world (Capitalizes first letter)
print(s.swapcase())  # HELLO WORLD -> hello world

