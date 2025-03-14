#empty list
# lst1 = []
#new_list
# lst2 = [1,5,3,15,9,11,72]
# #accesing elements in a list
# print(lst2[2]) #2nd element
# print(lst2[-1]) #last element

# #slicing a list
# # ✔ Slicing uses [start:end:step]
# # ✔ start is the index to start from
# # ✔ end is the index to end at
# # ✔ step is the number of elements to move
# print(lst2[2:5]) #start index 2, end index 5
# print(lst2[:4]) #start index 0, end index 4
# print(lst2[2:]) #start index 2, end index is the end of the list
# print(lst2[::2]) #start index 0, end index is the end of the list, step 2
# print(lst2[1::2]) #start index 1, end index is the end of the list, step 2
# print(lst2[::-1]) #reverse the list

#modifying lists
# lst2.append(10) #add 10 to the end of the list
# print(lst2)
# lst2.insert(2, 11) #insert 11 at index 2
# print(lst2)
# lst2.extend([12, 13, 14]) #add multiple elements to the end of the list
# print(lst2)
# lst2.pop() #remove the last element
# print(lst2)
# lst2.remove(9) #remove the first occurence of 9
# print(lst2)

#searching for an element in a list
# print(15 in lst2)
# print(lst2.index(15))

#sorting a list
# lst2.sort() #sort the list in ascending order
# print(lst2)

#list comprehension
# squared = [x**2 for x in range(10)]
# print(squared)