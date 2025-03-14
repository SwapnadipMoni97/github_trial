# def greeting(name):
#     print(f"hello {name}")
       
# greeting("Moni")
#----------------------------------------------------------------------------------------------------------
# define a greeting function that takes in a name and department            
# def greeting(name, department):
#     """ this function only returns None because it does not have a return statement"""
#     print(f"Hello, {name}, welcome to {department}")
    
    
# result =  greeting("Moni", "CSE") 
# print(result)       
#--------------------------------------------------------------------------------------------------------------
# define a add function that takes in two numbers and returns the sum
# def add(a, b):
#     return a + b

# result = add(2, 3)
# print(f"the sum is : {result}")
#---------------------------------------------------------------------------------------------------------------
# define a subtract function that takes in two numbers and returns the difference
# def subtraction(a, b):
#     return a - b

# result = subtraction(5, 3)
# print(f"the differnce is: {result}")
#---------------------------------------------------------------------------------------------------------------
#python functions accept any type of data
# def info(name, age):
#     print (f"hello,my name is {name} and I am {age} years old")
    
# print(info("Moni", 27))
#---------------------------------------------------------------------------------------------------------------
# define a function that takes in a list and returns the sum of the list
# def sum_of_list(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total
    
# result =  sum_of_list([1, 2, 3, 4, 5])
# print(result)
#---------------------------------------------------------------------------------------------------------------    
# list_1 = [1,2,3,4,5]

# for i in list_1:
#     print(i)
#---------------------------------------------------------------------------------------------------------------
# List_2 = [3,9,76,15,4,2,1,8,7,6,5]
# result = sorted(List_2)
# max_num = max(List_2)
# min_num = min(List_2)
# print(f"the maximum number is: {max_num}") 
# print(f"teh minimum number is : {min_num}") 
# print (f"the original list is: {List_2}")
# print(f"the sorted list is : {sorted(List_2)}")
# print(f"the soretd list is : {result}")
#---------------------------------------------------------------------------------------------------------------
# create functions with return values
# def area_of_triangle(base, height):
#      return 1/2 * base * height

# result = area_of_triangle(10, 5)
# print(f"the area of the triangle is : {result}") 
#===============================================================================================================
# fomatted strings f"{}" can take in any type of data
name = "moni"
age = 27
height =  5.9
list_1 = [1,3,6,8,9]

print(f"my name is {name} and I am {age} years old and I am {height} feet tall")
print(f"the original list is : {list_1} and the soretd list is : {sorted(list_1)}")
#-------------------------------------------------------------------------------------------------------------------