#A tuple is an immutable, ordered collection of elements.
#It is similar to a list, but once created, it cannot be modified (no add, remove, or change operations).

# Empty Tuple
t1 = ()

# Tuple with Elements
t2 = (1, 2, 3, "Python", True)

# Tuple without Parentheses (Packing)
t3 = 1, 2, 3  # Same as (1, 2, 3)

# Single-Element Tuple (Comma is Required)
t4 = (5,)  # Correct
t5 = (5)   # WRONG! This is just an integer.

# Tuple from Iterable
t6 = tuple([10, 20, 30])  # Converts list to tuple

# #accesing elements in a tuple
# t = ("apple", "banana", "cherry")
# print(t[0])   # apple
# print(t[-1])  # cherry

#Slicing

t7 = (10, 20, 40, 50, 70)
print(t7[1:4]) 