
# Program: Write a Python Program to create three dictionary and conatente them to create 4th dictionary.

fur = {
    "Apple": 4, "Banana": 6, "Mango": 56, "Graphes": 10

}

Ani = {
    "Lion": 45, "Tiger": 33, "Fox": 55
}

Pla = {
    "Thailand": 44,
    "India": 77,
    "U.S.A": 65
}

conc_dic = {**Ani, **Pla, **fur}            # First Method
print(conc_dic)

# Another method to do:

conc_dic_1 = {}
for d in (fur, Pla, Ani):
    conc_dic_1.update(d)
print("Another Method:")
print(conc_dic_1)

# Tips: 1.) From the output it can be observed that dictionaries are merged in the order that they listed in expression.
# 2.) Note that list of keys is constructed from a dictionary they are not stored in the oreder listed in expression.

# Program: Write a Program to check wheter a dictionary is empty or not.

d1 = {}
d2 = {
    "Name": "Aditi",
    "Surname": "Rathi",
    "Branch": "MCA",
    "Section": "A1"
}

if d1.items is True:
    print("Dictionary is not empty")

else:
    print("Dictioanry is empty")



# Checking for 'd2'
if d2.items is True:
    print("Dictionary is not Empty")

else:
    print("Dictiomary is not Empty")

# Another Method to Check is "bool"

print(bool(d1))                          # Output is False
print(bool(d2))                          # Output is True


# Program: Suppose there are two dictionaries called girls and boys contains name as key and thier age is value. Write a program to
# merged the two dictionary in third dictionary.

girls = {
    "Aditi": 22, "Radha": 12, "Anshika": 45, "Anju": 23
}

Boys = {
    "Raja": 45, "Mohan": 34, "Shivam": 23
}

Merged_dict = {}

for d in (girls, Boys):                        # Method "One"
    Merged_dict.update(d)
print("Merged Dictionary of Girls and Boys:")    
print(Merged_dict)


# Another Method:
Merged_dict1 = {**girls, **Boys}
print(Merged_dict1)

# Program: For the following dictionary write a Program to report minimum and maximum salary.

data = {
    "Aditi": {"Salary": 27000, "Age": 21, "Hieght": 5.6},
    "Shivam": {"Salary": 45000, "Age": 48, "Hieght": 6.7},
    "Tanu": {"Salary": 67000, "Age": 56, "Hieght": 5.3},
    "Subham": {"Salary": 78000, "Age": 56, "Hieght": 6.1}
}

print(max(data.items()))           # Here, python did not check salary, age, or height. it Only compares the name.
print(min(data.items()))           # Pyhton selecting the largest key(name), not salary.

# Finding maximum and minimum salary.
highest_salary = max(data.items(), key= lambda x: x[1]["Salary"])
print("Highest Salary is :")
print(highest_salary)

# For minimum Salary
print("Minimum Salary:")
print(min(data.items(), key= lambda x: x[1]["Salary"]))

# Explanation of terms under the code.

# Data.items()- gives (Names and deatils)
# x - one person
# x[1] - that person details
# x[1]["Salary"] -- that's person salary
# key - Tells Pyhton to compare salary 

