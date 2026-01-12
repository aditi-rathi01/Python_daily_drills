
#  ====== Sets ========


# Sets:- Sets are like lists, with an exception that they do not contain duplicate entries.

a = set()                  # empty set, use() instead of {}
b = {20}                   # Set, with one item.
c = {"aditi",2}            # Set, with multiple item.
d = {10,10,10,10,10}       # only 10 gets stored.

# Note: A Set uses hash value to store and find its element.
# hash value, is the address of element.

s = {12,23,45,16,52}          
t = {16,52,12,23,45}
u = {52,12,16,45,23}

print(s)                  # Output, is same for s,t,u which is {16,52,23,12,45}
print(t)                  # Output is same because the elements are same in all sets. 
print(u)                  # Same elements = Same hash value = Same storagre positions.

# Note: It is possible to create a set of strings and tuples, but not a set of lists.

s1 = {"Morining", "Evening"}
s2 = {(12,23),(15,25),(17,34)}
# s3 = {[12,23],[15,25],[17,34]}     # Shows, an error.

# Since, Strings and tuples are immutable, thier hash value always same. Hence a set of strings or tuples is permitted.
# However, a list may change, so its hash value may change, hence a set of lists is not permitted.

# Sets, are commonly to used for elemenating duplicate entries.


# ------- Accessing Set Elements ---------

# Entire set can be printed by just using the name of the set. Set is an unorderd collection. Hence order of insertion is
# not same as order of access.

s3 = {15,25,35,45,55}
print(s3)

# Being, an unorderd collection, items in a set cannot accessed using indices.
# Sets, cannot be sliced using [].


# ------- Looping In Sets ---------

# Like strings, lists and tuples, sets too can be iterated over using a for loop.

s3 = {15,25,35,45,55}
for i in s3:
    print(i)

# Note: unlike, string, list and tuple, a while loop should not be used to access the set elements. This is because
# we cannot access the set elements using an index, as in s[i].


# ------- Basic Set Opreations. -------

# Sets like lists are mutable. Their contents can be changed.

s4 = {"aditi","ram","shyam"}
s4.add("rathi")                  # Adds one more element to set s.
print(s4)

# If we want immutable Set, we should use a "frozenset".

s5 = frozenset({"Ram","aditi","python"})
# Now, it can't be modified.

# Two, sets cannot be concatenated using "+".
# While, converting a set using set(), repetitions are eliminated.

l = [10,20,10,30,40,50,30]
s6 = set(l)
print(s6)

# ------ Using Built-in Functions on Sets -------

# Many built-in fuctions can be used with sets.

s7 = {10,20,30,40,50}
print(len(s7))
print(max(s7))
print(min(s7))
print(sum(s7))
print(sorted(s7))

# Note: reversed() built-in function doesn't work on set.

# ------ Set Methods --------

# Any Set is an object of type set. Its methods can be accessed using the syntax s.method().

s8 = {12,15,13,23,22,16,17}
t1 = {"A", "B","C"}
u1 = set()

s8.add("Hello")
s8.update(t1)
s8.remove(15)
t1.clear()
print(s8)
print(t1)


# -------- Mathematical Set Opreations --------

# Following union, intersection and differnce opreations can be carried out on sets:

engineers = {"Vijay", "Sanjay","Ajay","Sujay","Dinesh"}
managers = {"Aditiya","Sanjay"}

# Union- all people in both categories.
print(engineers | managers)

# Intersection - Who are engineers and manager.
print(engineers & managers)

# Differnce - engineers who are not manager.
print(engineers - managers)

# Symmetric difference - managers who are not engineers and engineers who are not managers.
print(managers^engineers)

a = {1,2,3,4,5}
b = {2,4,5}
print(a>= b)


# ------ Set Varieties --------

# Unlike a list and tuple, a set cannot contain a set embedded in it.

# s = {"gate","name","age",{"roll no","class"}, "aditi"}              # error, nested set

# It's possible to unpack a set using the *opreator.

x = {1,2,3,4,5}
print(*x)


# ------- PRACTICE PROGRAM --------

# Program 1: What will the output of the following program ?
a = {10,20,30,40,50,60,70}
b = {33,44,51,10,20,50,30,33}

print(a|b)                        # Output: {10,20,30,40,50,60,70,33,44,51}
print(a & b)                      # Output: {10,20,30,50}
print(a-b)                        # Output: {40,60,70}
print(b-a)                        # Output: {33,44,51} 
print(a^b)                        # Output: {40,60,70,33,44,51}
print(a >= b)                     # Output: False
print(a <= b)                     # Output: False.


# Program: Write a program to carry out the following opreations on the given set
s9 = {10,2,-3,4,5,88}

# - Number of items in set S9
# - Maximum element in set s9
# - Minimum element in set S9
# - Sum of all elements in set s9
# - Obtain a new sorted set from s9 , set s9 remaning unchanged
# - report wheter 100 is an element of set s9
# - report wheter -3 is an element of set s9.

print(len(s9))
print(max(s9))
print(min(s9))
print(sum(s9))
print(sorted(s9))
print(100 in s9)
print(-3 in s9)

