#  ===== Program practice =====

# program A: What will be the output of the following programs.
msg1 = list("www.kicit.com")
print(msg1[-1])     
# My answer is 'm'


msg2 = list("kanlabs.teachable.com")
print(msg2[4:6])
# My answer is ['a','b']

msg3 = "Online Cousre - kanLabs"
print(list(msg3[0:3]))
# My answer is ['O','n','l']          

msg4 = "Rahate Colony"
print(msg4[-5:-2])
# My answer is "nol "          # The correct answer is "olo"

s1 = list("KanLabs")
print(s1[::-1])
# my answer is ["s", "b","a","L","n","a","k"]


num1 = [10,20,30,40,50]
num2 = num1
print(isinstance(num1,list))            # isinstance is used for check datatype of a variable. isinstance(variable, datatype)
print(num1 is num2)

a = [1,2,3,4]
b = [1,2,5]
print(a<b)

# The folowing code snipped code deletes elements 30 and 40 from the list:
num3 = [10,20,30,40,50]
del(num3[2:4])
print(num3)

# Another, method
num3[2:4] = []
print(num3)

# program: form the list given below
num4 = [10,20,30,40,50]
# How will you create the list num5 containg ["A","B","C",10,20,30,40,50,"Y","Z"]

num5 = ["A","B","C"] + num4 + ["Y","Z"]
print(num5)

# Program: Given list 
lst = [10,25,4,12,3,8]
# How will you sort it in descending order?

# Method 1: Using sort() 

lst.sort(reverse= True)
print(lst)

# Method 2: using sorted() (Original list not changed)
new_list = sorted(lst, reverse= True)
print(new_list)

# Method 3: Given a list 
lst = [10,25,4,12,3,8]
# How will you check wheter 30 present in the list or not?
print(30 in lst)

# How will you insert 30 between 25 and 4?
lst = lst.insert(2,30)
print(lst)

# Program : Given a string 
s = "Hello"
# How will you obtain a list ["H","e","l","l","o"]
s1 = [*s]
print(s1)

# program : suppose a list contain 20 integers genrated randomly. Receive a number from the keyboard and report all occurences of 
# this number in list.

import random
lst1 = [random.randint(10,100) for i in range(20)]
# print(lst1)

#num = int(input("Enter a number:"))

#for index, value in enumerate(lst1):
 #   if value == num:
  #      print("Found at position:", index)
        
   
# Program: Suppose a list has 20 numbers. write a program that removes all the duplicates from the list.

list1 = [12,24,36,48,60,72,13,26,36,55,48,13,24,77,66,23,26,55,23,99]


unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)


# Program: Suppose a list contains positive  and negative numbers. Write a program to create two lists- one containg positive
# number and another contain negative number.

lst2 = [0,23,-32,44,76,89,-98, 45,-65,-78,-18,30,34]

neg_list = []
pos_list = []

for i in lst2:
    if i>=0:
        pos_list.append(i)
    else:
        neg_list.append(i)
print("negative list:", neg_list)
print("Positive list:", pos_list)

# Progam: Suppose a list contains 5 strings. write a program to convert all these strings to uppercase.

s2 = ["aditi","mca","data scenece", "python","numpy"]
for i in s2:
    print(i.upper())        # Method to print outside the list.

s2 = ["aditi","mca","data scenece", "python","numpy"]
for i in range(len(s2)):
    s2[i] = s2[i].upper()

print(s2)


# Program: write a program that converts list of temperature in Fahrenheit degrees to equivalent celsius degrees.

temp = [97,90,92,93,94,96,98,99]         # Here, temperature is given in fahrenheit.

for i in range(len(temp)):               # formula for convsersion of f = (C*9/5)+32
    temp[i] = (temp[i] - 32)*5/9 
print(temp)

# Program: Write a program to obtain the median value of a list of numbers, without distrubing the order of the list.

list2 = [12,4,7,9,3]
list2.sort()
n = len(list2)
if n % 2 ==1:
    median = list2[n//2]
else:
    median = (list2[n//2-1]+ list2[n//2])/2

print("median:", median)