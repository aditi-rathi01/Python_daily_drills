# Problem: Suppose a dictionay contains roll number and name of students. Write a program to receive a roll no. , extracat
# the name corresponding to roll no. and display a message congratulating the students by name. If the roll number does
# not exists in the dictionary, the message should be 'congratualtion Student!'.

students = {
    25001: "Aditi Rathi",
    25002: "Aakash Sharma",
    25003: "Ruby Rajput",
    25004: "Shivam Chaudhary",
    25005: "Zoya Bharti"
}

#roll_no = int(input("Enter your Roll no."))

#name = students.get(roll_no, "Student")                     # Because, get() Always search for keys.
#print("Congratulations", name)                              # In the Synatx of name if we don't use "Student". then None will return.

# get() method used to take value from dictionary of a key which is given by us.
# for example: print(students.get("25001"))       ---- Output: It Will return "Aditi Rathi".


# Program: Write a Program that reads a string from from the keybaord and creates dictionary containg frequency of
# each character occuring in the string. Also print these occurrences in the form of a histogram.

d = {}
# string = input("Enter your String: ")                  # Let's take input of "Banana."

# for i in string:                            # Here, i worked as a key of dictionary 
  #  d[i] = d.get(i,0) + 1                   # d[i] means adding "key i" inside the dictionary. 
                                            # d.get(i,0) means return the value of i and if value not present in dictionary
                                            # then return 0. now in every condition add "+1". to value
                                            # In 'Banana' intially B is not present then, B -> (0)+ 1
                                            # similary for a-> (0) + 1, and when a comes again then a-> (1)+ 1 => 2
#print(d)

#for i, count in d.items():
 #   print(i, ":", "*"* count)               # i = This a Character (like "a","b","n")
                                            # ":" = Just a symbol to make output look nice
                                            # "*"* count = This means: repeat * count times.
# Output for the following:
# Enter your String: banana
# {"b":1, "a":3, "n":2}
# "b": *
# "a": ***
# "n": **


# Program: Given the following dictionary:
portfolio = {
    "accounts": ['SBI', 'IOB'],
    "shares": ['HDFC', 'ICIC', 'TM', 'TCS'],
    "ornamets": ['10 gm gold', '1 kg silver']
}

# Write a program to perfome the following opreations:
# - Add a key to portfolio called "MF" with values 'Reliance' and 'ABSL'.
# - Set the value of "accounts" to a list contaning "Axis" and "BOB".
# - Sort the items in the list stored under the "shares key".
# - Delete the list stored under 'ornaments' key.

portfolio["MF"] = ["Reliance", "ABSL"]
print(portfolio)

l = ["Axis", "BOB", *portfolio["shares"]]                # If we don't use "*" before protfolio then output come in nested list.
print(l)

print(sorted(portfolio["shares"]))

del(portfolio["ornamets"])                              # here, complete key "ornaments" will get deleted.
print(portfolio)                                   

# If simply want to delete the values of key instead of complete key. then the  method is:

portfolio["accounts"] = []          # for empty list value of key.
portfolio["MF"] = {}                # for empty dictionary of key.

print(portfolio)


# Program: Create two dictionaries- one containg grocery items and thier prices. and another contains grocires list and quantity
# purchased. By using the values from these two dictionaries compute the total bill.

list_mrp = {
    "Salt": 20, "soap" : 40, "vegetables": 70, "Juice": 50, "Milk": 33, "spices": 120, "flour": 56
}

list_quan = {
    "Salt": 4, "soap": 7, "vegetables": 12, "Juice": 1, "Milk": 2, "spices": 5, "flour": 3
}

total_bill = 0

for i in list_quan:                                 # We have taken list with quantity because quantity gives the values which 
    total_bill += list_mrp[i]* list_quan[i]         # we are added to our cart
print("Total Bill of Grocries: ", total_bill)

# print(list_mrp.items()*list_quan.items())           # Here, Pyhton throws an error because dict.items() conatin all key-value pair.
                                                      # dic[i] contains only the value of of "i key".

# Progaram : Which functions will you use to fetch all keys, all values and key-value pairs from a given dictionary.

dict1 = {
    "Aditi": 34, "Ram": 45, "Shyam": 24, "Priti": 66, "Shivam": 45, "Subham": 47, "Raja":33
}
print(dict1.items())
print(dict1.values())
print(dict1.keys())

# Create a dictionary of 10 username and passwords. Recieves the user name and password from the keyboard and search for 
# them in the dictionoray. Print appropirate message on the screen based on wheter a match is found or not.

data = {
    "Aditi Rathi": "Aditi@123", "Raj kumar": "Raj@123", "Rakesh": "Rakesh@123", "Radha": "Radha@123", "Harshita": "Harshita@123",
    "Shivam ": "Shivam@123", "Purab": "Purab@123", "Ramlaal": "Ramlaal@123", "Tanu": "Tanu@123"
}

name = input("Please, Enter your name: ")

if name in data:
    password = input("Enter your Password : ")

    if data[name] == password:
        print(name, ", welcome to Pyhton world")
    
    else:
        print("Invalid Password!, Try again")


else:
    print("User name not found ")


