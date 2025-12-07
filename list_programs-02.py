# ==== Practice Question ====

# program 1: Perfome the following opreations on a list of name: 
# - Create a list of 5 names - 'Anil', 'Anmol', 'Aditiya, 'Avi', 'Alka'
# - Insert a name 'Anuj', before 'Aditiya'
# - Append a name 'Zulu'
# - Delete 'Avi' from the list
# - Replace 'Anil' with 'AnilKumar'
# - Sort all the names in the list.
# - Print reversed sorted list.

list1 = ["Anil","Anmol","Aditiya","Avi","Alka"]
list1.insert(2, "Anuj")
list1.append("Zulu")
list1.remove("Avi")
list1[0] = "Anilkumar"
list1.sort()
print(list1[::-1])        # First Method to reverse the element
list1.reverse()           # Second Method to reverse the element
print(list1)



# Program 1.2: Perfome the following opreations on a list of numbers.
# - Create a list of 5 odd numbers.
# - Create a list of 5 even numbers.
# - Combine the two list.
# - Add prime number 11,17,29 at the beginning of the combined list.
# - Report how many element are present in the list 
# - Replace last 3 three numbers in the list with 100,200,300.
# - Delete the numbers in the list
# - Delete the list.


# Program  to create a list of 5 odd numbers.
l_odd = []
for i in range(10):
    if i % 2 != 0:
      l_odd.append(i)
print(l_odd)


# Program to create a list of 5 even numbers.
l_even = []
for i in range(10):
   if i % 2 == 0:
      l_even.append(i)
print(l_even)


# Program to create a combine list.
com_list = l_even + l_odd
print(com_list)


# program to add three prime numbers 11,17,29 at the beggining of the combined list
com_list.insert(0,11)
com_list.insert(1,17)    # Method one
com_list.insert(2,29)
print(com_list)       

# Method two
com_list = [11,17,29]+ com_list



# Program to report how many elements are present in the list.
print(len(com_list))      # method one

count = 0
for i in com_list: # method 2
   count +=1
print(count)


# Program to replace last three numbers in the list with 100,200,300.
com_list[10] = 100
com_list[11] = 200
com_list[12] = 300
print(com_list)


# Program to delete all the elements in list.
com_list = []
print(com_list)


# program to delete the list.
del com_list


# Program 3: Write a program to implement a Stack data strucutre. Stack is a Last in First Out (LIFO) list in which addition and 
# deletion takes place at the end takes place at the same end.

s = []
# Push element in stack
s.append(10) 
s.append(20)
s.append(30)
s.append(40)
s.append(50)
print(s)

# Pop element from the stack
print(s.pop())
print(s.pop())
print(s.pop())
print(s)


# program 4: Write a program to implement a Queue data strucutre. Queue is FIFO list, in which addition takes place at the 
# rear end of the queue and deletion takes place at the front end of the Queue.

import collections
q = collections.deque()

q.append("aditi")
q.append("rathi")
q.append("data science")
q.append("MCA")
q.append("Noida")
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft)
print(q)


# WAP to generate and store in a list 20 random numbers in the range 10 to 100. From the list delete all the entries which have
# between 20 and 50. print the remaing list.

import random
ran_list = []
for i in range(20):
    num = random.randint(10,100)
    ran_list.append(num)
print(ran_list)


for num in ran_list:
    if num>20 and num<50:
        ran_list.remove(num)
print(ran_list)


