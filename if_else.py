# print(10>1)
# print(10<1)
#---------------------------------------------------------------------------------------------------------------
# def comparison(a, b):
#     """ This function takes 2 numbers and compares tnem and retuend us the result"""
#     if a > b:
#         return f"{a} is greater than {b}"
#     elif a < b:
#         return f"{a} is less than {b}"
#     else:
#         return f"{a} is equal to {b}"

# result = comparison(5, 5)
# print(result)
#---------------------------------------------------------------------------------------------------------------
#now take runninng input from the user
# def comparison():
#     """ This function takes 2 numbers and compares tnem and retuend us the result"""
#     a =  int(input("Enter the first number: "))
#     b =  int(input("Enter the second number: "))
#     if a > b:
#         return f"{a} is greater than {b}"
#     elif a < b:
#         return f"{a} is less than {b}"
#     else:
#         return f"{a} is equal to {b}"
    
# print(comparison())
#---------------------------------------------------------------------------------------------------------------
#a simple function to check if the username is bigger than 3 and less than 6
def username(username):
    if len(username) < 3:
        return f"the username {username} is invalid"
    elif len(username) > 6:
        return f"the username {username} is invalid"
    else:
        return f"the username {username} is valid"
    
# result = username("swapnadip")    
# print(result) 

print(username("sw"))
print(username("swap"))
print(username("swapna"))
print(username("swapnadip"))
print(username("Mo"))
print(username("Moni"))
#---------------------------------------------------------------------------------------------------------------