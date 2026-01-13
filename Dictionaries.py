# ====== Dictionaries ======

# A dictionary is a collection of key - value pairs.
# Dicitonary are also known as maps or associative arrays.

d1 = {}          # Empty Dictionary
d2 = {"A01": "Anmol", 
      "A02": "Anil",
      "A03": "Ravi"}

# Here, A01, A02, A03 are the keys and "Anmol","Anil" and "Ravi" are the values.

d3 = {10: "A",
      20: "B",
      30: "C"}  # Different keys have the same value.

# Keys must be unique. If keys are same, but values are different, latest key value pair gets stored.

d4 = {10:"A",
      20:"B",
      10:"A"}        # If the key value pair are repeated, then only one pair get stored.
print(d4) 


# ----- Accessing Dictionary Elements ------

# Entire dictionary can be printed by just using the name of dictionary.
print(d1)

# Unlike sets, dictionaries preserve insertion order. However, elements are not accessed using the position(index),
# but using the key.

d2 = {"A01": "Anmol", 
      "A02": "Anil",
      "A03": "Ravi"}

print(d2["A01"])               # Prints, the value for key "A102".

# Thus, elements are not position indexed, but key indexed.
# Dicitionary cannot be sliced using [].


# ------- Looping in Dictionaries --------

# Like strings, lists, tuples and sets, dictionaries too can be iterated over using a for loop. There are three ways to do
# so:

dict1 = {
    "Name": ["Aditi","Ram", "Sham","Gyan", "Radha","serya"],
    "Course": ["mca","m.tech", "B.sc", "B.tech", "Mba","bca"],
    "Age" : [34,23,53,34,24,46],
    "Address": ["Mumbai","Noida","Punjab","Mathura","Delhi", "Banglore"]
}
print(dict1)

# Iterate over Key-values Pairs:

for k,v in dict1.items():
    print(k,v)

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

# While, iterating through a dictionary using a for loop, if we wish to keep track of index, we can use enumerate() function.

dict1 = {
    "Name": ["Aditi","Ram", "Sham","Gyan", "Radha","serya"],
    "Course": ["mca","m.tech", "B.sc", "B.tech", "Mba","bca"],
    "Age" : [34,23,53,34,24,46],
    "Address": ["Mumbai","Noida","Punjab","Mathura","Delhi", "Banglore"]
}

for i, (k,v) in enumerate(dict1.items()):
    print(i,k)


# ------- Basic Dictionary Opreations -------

# Dictinoray are mutable. So, we can perfome add/delete/modify opreations on a dictionary.

stud_det = {
    25001: "Aditi",
    25002: "Badal",
    25003: "Ram",
    25004: "Shyam"
}

print(stud_det)

# Add, Modify, delete
stud_det[25005] = "Raja"       # add new key-value pair.
stud_det[25002] = "Radha"      # Modifies value for key.
del(stud_det[25002])           # Delete a key-value pair.
del(stud_det)                  # delete complete dictionary.

# Note That any new addition will take place at the end of existing dictionary.
# dictionary keys cannot be changed in placed.

# Two dicitionary cannot be concatenated using +.
# two dicitionary cannot be merged using z = t + u.
# Two dicitionary objectes cannot be compared using <,>.
