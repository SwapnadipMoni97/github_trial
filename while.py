####################################################################################################
# def sum_of_numbers(numbers):
#     total_sum = 0
#     index = 0

#     while index < len(numbers):
#         total_sum += numbers[index]
#         index += 1

#     return total_sum

# numbers = [1, 2, 3, 4, 5]
# result = sum_of_numbers(numbers)
# print("The sum of the numbers in the list is:", result)
#####################################################################################################
#use while loops to iterate through a list
# def sum_of_numbers_of_a_list(numbers):
#     """ This function takes in a list of numbers and returns the sum of the numbers"""
#     total_sum = 0
#     i = 0
#     while i < len(numbers):
#         total_sum += numbers[i]
#         i += 1
#     return total_sum

# result = sum_of_numbers_of_a_list([3, 5, 8, 14, 25])
# print(f"the sum of the numbers in the list is : {result}")
#####################################################################################################
#print sum of even numbers from 1 to 10

# even_sum = 0
# i = 0
# while i <= 10 :
#     if i%2==0:
#         even_sum += i
#     else:
#         pass
#     i += 1         
    
# print(f"the desired sum is {even_sum}") 
######################################################################################################
#count odd numbers between 1 to 20

odd_count = 0

i = 0

while i <= 20 :
    if i % 2 != 0:
        odd_count += 1
    else:
        pass
    i += 1
    
print(f"The odd count is {odd_count}") 

########################################################################################################      