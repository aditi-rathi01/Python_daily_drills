# ====== Dictionaries ========

d = {
    "A001": "Aditi",
    "A002": "Shivam",
    "A003": "shaym",
    "B002": "Rajunath",
    "A004": "Rahul",
    "A005": "Radha"
}

# ------- Using Built-in Functions on Dictionaries.-------

# Many built-in fuctions can be used with dictionories.

print(len(d))                    # Return number of keys-value pair
print(max(d))                    # Return Maximum key in dictionary d. (Return: B001)
print(min(d))                    
print(sorted(d))              
 # print(sum(d))                   # Return sum of all keys if keys are numbers.
print(any(d))
print(reversed(d))

# Use of reversed function to reverse a dictionary by keys is shown below:

for k,v in reversed(d.items()):
    print(k,v)


# ----- Dictionary Methods ---------

# There are many dictionary methods. Many of the opreations performed by them can also be perfomed using built in functions.
# The useful dictionary methods are shown below:

a = {
    "MCA01": "Aditi",
    "MCA02": "Badal",
    "MCA03": "Riya",
    "MCA04": "Subham"
}

b = {"BCA01": "Archna",
     "BCA02": "prena",
     "BCA03": "Ram"
     }

print(a.get("MCA02","Absent"))     # Print the value of "MCA02" if it exists, otherwise print "Absent"
print(a.get("MCA09", "Absent"))    # Print "Absent". because "MCA09" is not present in the 'a' dictionray. 
#                                     If "Absent" is not written in code than, it prints "None".


# Note: If we directly write print(a["MCA09"]) it raises keyerror. so, our code does not move further.

print("Updating a with items in b:")
c = a.update(b)                         #  If we print c then it gives "None". Because, actuall changed in dic "a".
print(a)


# ------- Dictionary Varieties -------

# Keys in a dictionary must be unique and immutable. Numbers, tuples and string can be used as keys, it should not contain 
# any mutable elements like list.

d1 = {
    (1,5): "Aditi",
    (2,7): "Ram",
    (4,6): "Sham"
}

# Dictionries can be nested,

contacts = {
    "Anil": {"DOB": "17/11/98", "Surname": "Aakash"},
    "Rajeev": {"DOB": "02/4/99", "Surname": "Rakesh"}
}

print(contacts)

# Two dictionary can be merged to create third dicitionary by unpacking the two dictionaries using **.
# If we use only * only keys will unpacked.

Animals = {
    "Tiger" : 3, "Lion": 4, "Zeraf": 5
}

Birds = {
    "Parrot": 2, "Eagle": 1, "Crow": 5
}

Combined =  {**Animals, **Birds}
print(Combined)


# ------ fromkeys() function -------

# A dictionary can be created in which the keys are the different but the values of key are same.

lst = ["Aditi", "Rathi", "mca", "Python"]

dic = dict.fromkeys(lst, 25)
print(dic)

# Program 1: Create a dictionary called student containg names and ages. copy the dictionary into stud. Empty the students
# dictionary , as stud contionus to hold the data.

student = {
    "Stud1": {"Name": "Aditi Rathi", "Age": 21},
    "Stud2": {"Nmae": "Raju Sharma", "Age": 45}
}

stud = student        # Shallow copy

student = {}
 
# If we use stud.clear() it would cleared all data, So student and stud both become empty dictionary.

# Program: Create a list of criketrs, Use this list to create a dicitionary in which the list value became the keys of dictionary
# Set all the values of keys to 50 in the diciionary created.

l_crik = ["Virat", "Sachin", "M.S. Dhoni", "Yuvraj", "Virat", "M.S. Dhoni"]

dict1 = dict.fromkeys(l_crik, 50)
print(len(l_crik))                               # Output : len of list is 6
print(len(dict1))                                # Output : len of dict1 is 4.
print(dict1)


# Tip: # we already know that keys of dictionary are unique. Since, list may contain duplicate elements. then when converting
# list into dictionary all dupicates elements or keys get removed automatically.


# write a program to sort a dictinoary in ascending order ascending/descending order by key and ascending/decsending order by 
# values.

dict2 = {
    "Aditi": 78,
    "Ram": 18,
    "Subject": 100345,
    "Branch": 67,
    " ":  2209
}

print("Original Dicitonary", dict2)

dict3 = sorted(dict2.items())
print("Ascending Order of key: ", dict3)
dict4 = sorted(dict2.items(), reverse= True)
print("Descending order of keys are:", dict4)
 
# Sorting by value.
import operator
dict5 = sorted(dict2.items(), key= operator.itemgetter(1))
print("Ascending order :", dict5)

dict6 = sorted(dict2.items(), key= operator.itemgetter(1), reverse= True)
print("Descending order :", dict6)


# Note: 
#  By default, items in a dictionary would be sorted as per the key.
# To store values we need to use opreator.itemgetter(1).
