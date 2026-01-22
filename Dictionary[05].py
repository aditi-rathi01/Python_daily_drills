
# Program: Given the following dictionary
marks = {
    "Subu": {"Maths": 88, "Eng": 60, "SSt": 95},
    "Anmol":{"Maths": 78, "Eng": 68, "SSt":89 },
    "Raka":{"Maths":56, "Eng": 66, "SSt":77 }
}
# Write a program to perfome the following opreations:
# - Print marks obtained by anmol in english.
# - Set marks obtained by raka in Maths to 77.
# - Sort the dictionary by name.

print("Marks obtained by Anmol in English : ", marks["Anmol"]["Eng"])
marks["Raka"]["Maths"] = 77
print("Updated Raka Marks in Maths:", marks["Raka"]["Maths"])
print("Sorted Dictionary by Name", sorted(marks))


# Program: Suppose a dictionray conatains 5 key-value pairs of name and marks. Write a program to print them from last pair to
# first pair. keep deleting every pair printed, such that the end of printing the dictionary falls empty.

data = {
    "Adiit": 98, "Raju Ghandi":88, "Riya Tomar": 45, "Janvi Kapoor": 68, "Radhika": 55
}

# Print from last to first.
for key in reversed(data):                        # Reversed is a function, not an action by itself.
    print(key, ":", data[key])



# Program: What will be the output of the following code snipped ?

d = {"Milk":1, "Soap": 2, "Towel": 3, "Shampoo": 4, "Milk": 7}

# print(d[0], d[1], d[2])   --> Thorws an error. because indexing are not apply on dictionary.





# ======= End of Dictionary =========
