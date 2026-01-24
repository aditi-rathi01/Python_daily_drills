# ======= Comprehension =======

# Comprehension is a short and smart way to create collections(like lists, sets and dictionaries) ib one line instead.

# why do we use Comprehension.?
# - Code becomes shorter
# - Code becomes cleaner


# For Example:
#  Noraml way: 
Squares = []
for i in range(1,6):
    Squares.append(i*i)
print(Squares)


# Using list Comprehensions:
squares = [i*i for i in range(1,6)]
print(squares)


# ------- List Comprehensions ------

# So, generall form of list compreshisons is 
# lst = [expression for var in sequence [optional  for and/or if]]

# Example of list comprehensions:

# generate 20 randoms numbers in the range 10 to 100.
import random
from random import randint
lst = [random.randint(10,100) for n in range(20)]
print(lst)

# genreate square and cube of all numbers between 0 to 100
lst2 = [(x, x**2, x**3) for x in range(10)]
print(lst2)

# Convert a list of strings to a list of integers.
lst3 = [int(x) for x in  ["10", "20", "30", "40"]]
print(lst3)


# Examples of use of if in list comprehensions.

# genreate a list of even numbers in the range 10 to 30
lst4 = [n for n in range(10,30) if n% 2 == 0]
print(lst4)


# {  // Rule for writing list comprehension //

#   expression -> for -> if

# Or we can say that:

# Expression
# for loop 
# If condition  }

# {  In One Condition When if-else both are used, place them before for. }

# Example of use of if-else in list comprehensions:

# Replace a vowel in a string with !.
lst5 = "".join(["!" if ch in "aeiouAEIOU" else ch for ch in "Aditi Rathi"])
print(lst5)

# Meaning of Code: 
# "" :- This means nothing(no spaces, no character) Use it because we want: charcaters to be joined without any space.
# Example: print("".join("A", "D", "I","T","I"))              # Output is ADITI


# Example of Use of multiple fors and if in list comprehension:

# Flatten a list of lists.
arr = [[1,2,3],[4,5,6],[7,8,9]]
b = [*arr[0], *arr[1], *arr[2]]
print(b)

# Note The differnce between nested for in a lisst comprehension and a nested comprehension.

# produce [4,5,6,5,6,7,6,7,8]
lst6 = [a+b for a in [1,2,3] for b in [3,4,5]]
print(lst6)

# Produce [[4,5,6], [5,6,7],[6,7,8]]
lst7 = [[a+b for a in [1,2,3]] for b in [3,4,5]]
print(lst7)

# Example of use of multiple fors and if in list comprehension:

# generate all unique combination of 1,2 and 3

a = [(i,j,k) for i in[1,2,3] for j in [1,2,3] for k in [1,2,3] if i !=j and j != k and k != i]
print(a)

