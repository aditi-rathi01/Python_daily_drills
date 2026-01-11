# === Tuples ====

# Program 4: A List contain tuples containg roll no., name, age. write a python progam to gather all name from the list
# into another list.

lst = [("A01","Aditi", 22),("A02","subham", 21),("A03","Shivam", 20),("A04", "Ram", 56)]

lst1 = []
for i in lst:
    lst1 = lst1 + [i[1]]
print("print lst1:" ,lst1)          # Method "1"

lst2 = []
n = 0
while n< len(lst):
    lst2.append(lst[n][1])
    n = n+1

print("Print lst2 :" ,lst2)       # Method "2"


# Program 5: Given the following tuple
# ("F", "I", "a", "b","b","e", "r","g", "a","s","t","e","d" )

# write a pyhotn program to carry out the following operations:
# - Add an ! at the end of the tuple.
# - Convert a tuple to a string.
# - Extract ("b","b") from the tuple
# - Find out number of occurrences of "e" in the tuple 
# - Check wheter " r" exists in the tuple.
# - Convert the tuple to a list
# - Delete characters "b","b","e", "r" from the tuple.

tpl = ("F","I", "a", "b","b","e","r","g","a","s","t","e","d")

print(tpl + ("!",))


# Method "1" to convert it into string.
string = "".join(tpl)                   # Output: FIabbergasted
print(string)

str2 = " ".join(tpl)                    # Output: F I a b b e r g a s t e d 
print(str2)

str3 = ",".join(tpl)                    # Output: F, I, a, b, b,e, r,g,a,s,t,e,d
print(str3)                 

# Method "2":
str4 = ""
for i in tpl:
    str4 +=i
print(str4)


# Extract ("b","b") from the tuple
for i in tpl:
    if i == "b":
        print((i,i))
        break


# Finding occerence of "e" in tuple.

for i in tpl:
    if i == "e":
        print("yes, there is occurence of 'e'")

# To, count number of "e" in tuple.

app_e = tpl.count("e")
print("Total Number of Apperance of 'e':", app_e)

# Check wheter "r" appear in tpl.

for i in tpl:
    if i == "r":
        print("Yes, 'r' apperas in tpl")

# Convert a tuple into a list.

tpl = list(tpl)                 # Method "one"
print(type(tpl))

l = []
for i in tpl:
    l.append(i)
print(l)

# Delete "b","b","e","r" from the tuple.

# Since, tuples are immutable then cannot be deleted, add or change.
# there are two ways to delete the elements.
# First, method is to convert tuple into list. and then deletion.
l.remove("b")
l.remove("e")
l.remove("b")
l.remove("r")
print(l)


# We, need to split the tuples.

tpl = tpl[:3]+ tpl[7:]
print(tpl)


# Question: Which of the following properties apply to string, list, tuple.
# - Iterable
# - Sliceable
# - Indexable
# - Immutable
# - Sequence
# - Can be empty
# - Sorted collection
# - orderd collection
# - unorderd collection
# - Elements can be accessed using the position in the collection.

# Answer:
# LIST = [Iterable, sliceable, indexable, can be empty, sorted collection, orderd collection, elements can be accessed]
# TUPLES = [Iterble, Sliceable, Indexable, sequence, Immutable, can be empty, stored collection, orderd collection, elements acess]
# String = [Iterable, Sliceable, Indexable, Immutable, Sequence, can be empty, sorted and orderd collection, elemts access]


# Program: Suppose a date is representd as a tuple(d,m,y). Write a Program to create two dates tuple and find the number 
# of days between the two dates. 

tpl1 = (1,9,2003)
tpl2 = (22,9,2003)

tpl3 = tpl2[0] - tpl1[0]
print("Day Differnce is: ", tpl3)

tpl3 = (3,10,2004)
tpl2 = (22,9,2003)

from datetime import date

tpl3 = (3,10,2004)
tpl2 = (22,9,2003)

date1 = date(tpl3[2], tpl3[1], tpl3[0])
date2 = date(tpl2[2], tpl2[1], tpl2[0])

days = abs((date2 - date1).days)
print("Days between two dates:", days)