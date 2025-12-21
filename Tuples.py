
 # ===== Tuples ======


# A tuple is orderd and immutable and collection of elements in Python, used to store multiple values in a single variable.
# orderd --> each element has a fixed position and can be accessed using its index.

a = ()          # empty tuple.
b = (10,)       # tuple with one item. , after 10 is neccessary.
c = (8)         # It is considerd as type int.

# Items in a tuple can be repeated, i.e., tuple may contain duplicate items. Like list, tuple elements can be repeated 
# using a*

tup1 = (10,)*5      # stores (10,10,10,10,10)
tup2 = (10)*5       # stores (50)
print(tup1)
print(tup2)

# // // Accessing Tuple Elements

# like string and list, tuple items accessed to using indices, starting with 0.

msg = ("hello","world","aditi","rathi","mca","data science")
print(msg[1], msg[3])

# Tuples are sliced too.
msg2 = ("aditi","rathi", "mca","Python","java","c++","stat")
print(msg2[:2])
print(msg2[2:4])
print(msg2[::-1])
print(msg2[5:2:-1])

# // // Looping in Tuples.

tpl = (10,20,30,40,50,60)
i = 0
while i< len(tpl):
    print(tpl[i])
    i +=1

for i in tpl:
    print(i)

# If we wish to tack the index of element. we can do it with the help of enumerate.

for index, value in enumerate(tpl):
    print(index, value)

# // // Basic Tuple opreation.

tpl2 = (12,24,36,48,60,72,84)

#     tpl2[2] = 33        Throughs as an error because tuples are immutable.


# // // Changing a Tuple.

# mutable list and immutable string - all belong to tuple.

tpl3 = ([1,2,3,4,5],[7,2],"aditi")
tpl3[0][1] = 100
print(tpl3)


# // // Using Built-in Functions on Tuples.

tpl4 = (12,32,10,45,55,90)
print(max(tpl4))
print(min(tpl4))
print(sum(tpl4))
print(sorted(tpl4))


# // // Tuple Methods

tpl4 = (12,32,10,45,32,44,55,32,90)

print(tpl4.count(32))                  # Return number of times 32 present in tpl4
print(tpl4.index(10))                  # Return index number of item 10
# print(tpl4.index(400))               # Throughs an error, because 400 is not present in the tpl4


# // // Tuple Varieties.

a1 = (10,20,30,40,50)
b1 = (55,3,2,11,90)

# It's possible to create a tuple of tuples.

c1 = (a1, b1)
print(c1)

print(c1[0][3],c1[1][2])

records = (
            ("aditi", 22, 4848), ("shivam", 20, 5000),
            ("priyanka", 33, 3600), ("ram", 76, 5004)
)

print(records)
print(records[0][2], records[0][0][2], records[3][2])

# A tuple may be embedded in another tuple.

tpl5 = (10,20,30,78,18,60)
tpl6 = (1, 2, 3, tpl5, 7)
print(tpl6)

# Note: It is possible to unpack a tuple using the *operator.

tpl7 = (56, 34, 23, *tpl5, 7)              # Output is (56,34,23,10,20,30,78,18,60)
print(tpl7)

tpl8 = (1, 2, 3, *tpl6, 8)                 # Output is (1,2,3,1,2,3,(10,20,30,78,18,60),7,8)
print(tpl8)

# Note: It is possible to create a list of tuples, or a tuple of lists.



# If we wish to sort a list of tuples, and tuples of list, it can be done as follow:
import operator
lst = [("shailesh", 24, 8758.78),("Arjun", 56, 90000.65)]
tpl9 = (["shailesh", 24, 8758.78],["Arjun", 56, 90000.65])
print(sorted(lst))
print(sorted(tpl9))      # By, default, sorted() sort first item in list.
print(sorted(lst, key= operator.itemgetter(2)))    # Will give us a fuction that fatches salary from a list.



# Progam 1: Pass a tuple to the divmod() function and obtain the quotient and the remainder.

# dimvod() is a built-in that returns two variables at the same time:
# 1. Quotient()        // --> Quotient
# 2. Remainder()       % --> Remainder.

# divmod(a,b) --- (Quotient, Reaminder)

result = divmod(23,11)
print(result)

t = (12,5)
# result2 = divmod(t)   # If we pass t directly to divmod() an error is reported. We have to unpack the tuple into two distinct value.
result3 = divmod(*t)
print(result3)

# Problem 2: Write a Pyhton Program to perfome the following opreations:
# - Pack first 10 multiples of 10 into a tuple.
# - Unpack the tuple into 10 variables, each holding 1 value.
# - unpack the tuple such that first value get stored in the variable x, last value in y and all the values into between
#   into disposable variables.
# - unpack the tuple such that first value gets stored in variable i, last value in j and all values in between into a single
#  disposable variables.


t1 = tuple(i*10 for i in range(1,11))
print(t1)
a,b,c,d,e,f,g,h,i,j = t1      # To unpack the value inside the tuple we use this method.
print(a)
print(f)
print(i)

x, *_, y = t1
print(x,y,_)

# Program 3: A list contain names of boys and girls as its elements. Boy's name stored as a tuples. Write a Pyhon Program
#            to find out number of boys and girls.

l = ["aditi", "sherya",("shivam",), "Taniya",("Ram",),"Payal", ("raju",)]
boys = 0
girls = 0
for i in l:
    if isinstance(i, tuple):
        boys +=1
    else:
        girls +=1
    
print("No. of boys:", boys)
print("No. of girls:", girls)

# isinstance() fuctions check wheter a element is an instnace of tuple type...