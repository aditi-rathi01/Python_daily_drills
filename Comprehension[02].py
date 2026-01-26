# -------- Set Comprehension ---------

# Like, list comprehension, set comprehension offer an easy way of creating sets. 
# So, genreal form of a set comprehension is
# s = {expression for var in sequence [optinal for and/or if]}.

# Example of set comprehension:

# generate a set containing square of all numbers from 1 to 10:

a = {i**2 for i in range(1,11)}
print(a)

# from a set delete all numbers between 20 and 50.

a1 = {i for i in a if i<20 and i>50 }
print(a1)

# ----- Dictionary Comprehension --------

# Genreal form of dictionary comprehensions is as follow:
# dic_var = {key:value for (key, value) in dictionary.items()}

# Example of dictionary comprehension:

d = {"a":1, "b":2, "c":3, "d":4}

# Obtained dictionary with each value cubed.

d1 = {k:v**3 for (k,v) in d.items()}
print(d1)

# Obtain dictionary with each value of cubed if value>3

d2 = {k:v**3 for (k,v) in d.items() if v>3}
print(d2)

# Identify even and odd among the each value of dictionary.

d3 = {k:("Even" if v % 2 ==0 else "Odd") for (k,v) in d.items()}
print(d3)


# Program: Using list comprehension, write a progaram to generate a list of numbers in the range 2 to 50 that are divisble
# by 2 and 4.

l = [i for i in range(2,51) if i%2 == 0 and i%4 == 0]
print(l)

# Program: Write a Program to flatten the following list using list comprehension

lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

flat_list = [i for sublist in lst for i in sublist]
print(flat_list)

# for sublist in lst -> Goes through each element from that inner list
# for item in sublist -> Takes each element from the inner list
# i -> collects all elements into one single list.


# Program: Write a program to create a set containg some randomly generated numbers in the range 15 to 45. Count how many
# of these numbers are less 30. Delete all numbers which are less than 30.

import random
s = {random.randint(15,45) for i in range(20)}
print(s)

# Counting numbers < 30
sum(1 for x in s if x <30)

# Removing numbers < 30

s1 = {x for x in s if x > 30}
print(s1)

