# ---- LISTS ----


# Python has the following container data types: 
#  Lists     Tuples
#  Sets      Dictionaries

l1  = ["aditi", "shivam", "mca", "python","data_science", 78, 12.98, True]
print(l1[0:4])  # Like string, list are also sliced.

# Looping in list.
l2 = ["delhi", "noida", "mumbai", "Bhopal","lucknow", "indore","punjab"]

i = 0
while i<len(l2):        # Using while loop
    print(l2[i])
    i +=1

for j in l2:            # Using for loop
    print(j)

# // Note: while itreating through a list using for loop, if we wish to keep track of the index of element that j referring to,
#          we can do so using built in enumerates() function.

l2 = ["delhi", "noida", "mumbai", "Bhopal","lucknow", "indore","punjab"]
for index, a in enumerate(l2):
    print(index, a)


# Mutabilty: Unlike strings, lists are mutalbe(changeable).

l3 = ["aditi", "riya", "shivam","jaya","mukesh","rajeev", "abhay"]
l3[1] = "archana"   # It, will replace riya's name with archana's name.
print(l3)

l3_ages = [22,54,21,65,44,36,66]
l3_ages[2:5] = [10,10,10]   # It will replace direct 3 numbers.
print(l3_ages)     

l3_ages[0:2] = []  # It combainly delete 2 and many elements in a sequence. 
print(l3_ages)  

# Concatination: One list can be concatenated(appended) at the end of another.

l3_ages = l3_ages + [22,45,67,78,18]
print(l3_ages)

# merging: Two list can be merged

l4 = l3 +l3_ages   # merging two list.
print(l4) 

# Conversion: A string/tuple/set can be converted into a list using the list() conversion function.
l = list("africa")
print(l)      # Split every single word as a element of list.

# Cloning: This involves copying contents of one list to another list, after copying both refer to differnt lists.

l5 = ["C_Programming", "Mathematics", "Cyber_security", "COA", "FCET", "profesional_communincation"]
l6 = []
l6 = l5 + l6
print(l6)


# searching: An element can be searched in list using the membership opreator

l7 = ["a","e","i","o","u"]
print("i" in l7)
print("j" in l7)

# identity: Whether the two variables are referring to the same list can be checked using the is identity opreator.

l8 = [10,20,30,40,50]
l9 = [10,20,30,40,50]
l10 = l8
print(l8 is l9)
print(l8 is not l9)


# Comparison: It is possible to compare contnets of two lists. comparison is done item by item till there is mismatch

l11 = [1,2,3,4,5]
l12 = [1,2,6]
print(l11<l12)

# empitness: We can check if a list is empty using not opreator.

l13 = []
if not l13:
    print("empty list")

l14 = [10,20,30,40,50]
# built in fuction

print("sum:", sum(l14))
print("max:", max(l14))
print("min", min(l14))
print("sorted", sorted(l14))

del(l14[2])
print(l14)
del(l14[1:2])
print(l14)


# Note: If multiple variables are reffering to same to list, then deleting one doesn't delete the others.

l15 = ["aditi", "Python", "cyber_security", "data_science"]
l16 = l17 =l18 = l15      # all refer to same list.
l15 = []
print(l15)
print(l16)
print(l17)
print(l18)

# if multiple variables reffering to same to list and we wish to delete all. then it can be done:

l16[:] = []   # list is empited by deleting all items.

print(l15)    
print(l16)
print(l17)
print(l18)

# // List methods.

l19 = [12,24,36,24,45,13,77,90]
l19.append(23)                       # Add new element at the end to list.
l19.remove(36)                       # delete item 36 from list
# l19.remove(100)                      # Reports valueError as 100 in absent in l19
l19.pop()                            # always, remove last element of l19
l19.insert(2,50)                     # insert a number 50 in index number 2
l19.count(24)                        # return of element occerence
idx = l19.index(45)                  # return the index value in which 45 value occur

# // Sorting and reversing
l20 = [78,18,23,45]
l20.sort()
l20.reverse()
print(l20[::-1])                    # same as revers of string.


# // Nested list

y = [1,2,3,45,22,445,67]
x = ["aditi","rathi", "noida","data","science",y]
print(x)


# It is possible to unpack a string or list within a list using the * opreator

s = "hello_world"
l21 = [*s]
print(l21)
