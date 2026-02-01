
# Program: Write a program that defines two functions called create_sent1() and create_sent2(). Both recieve following 3 list:
subjects = ["He", "She"]
objects =  ["loves", "Hates"]
verbs  = ["Serial", "Netflix"]

# Both functions should form sentence by picking elements from these lists and return them. Use for loops in create_sent1()
# and list comprehension in create_sen2().

def create_sent1(subjects, objects, verbs):

    sentences = []

    for i in range(len(subjects)):
        for j in range(len(objects)):
            for k in range(len(verbs)):

                sentences.append(subjects[i]+ " "+ verbs[j] + " " + objects[k])

    return sentences


print(create_sent1(subjects, objects, verbs))


# Prpgram: Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of 
# uppercase and lowercase alphabets in it. It should return these values as a dictionary. Call this function for some sample
# String.

def count_lower_upper(s):

    d = {"Uppercase": 0, "Lowecase": 0}

    for ch in s:
        if ch.isupper():
            d["Uppercase"] += 1
        
        elif ch.islower():
            d["Lowecase"] += 1


    return d

#string = input("Enter Your String: ")
#print(count_lower_upper(string))


# Program: Write a Program that defines a function compute() that calculates the value of n + nn + nnn + nnnn, where n is a digit
# recieved by a function. Test the function for digits 4 and 7.

def compute(n):

    result = n + n**2 + n**3 + n**4

    return result

#num = int(input("Enter a Number: "))
#print(compute(num))


# Program: Write a Program that defines a function create_array() to create and return 3D array whose diminsions are
# Passed through to the function. Also initalize each element of this array to a value passed to the function.

def create_array(x,y,z, value):         # x = number of layers(depth/ 3D dimensions)
                                        # y = Number of rows,  z = Number of columns, value = value to fill everywhere
    arr = []

    for i in range(x):                  # loop run 'x' time, Each loop create one 2D block
        block = []                      # Creates an empty list for one layer(2D array) 

        for j in range(y):              # Loop run 'y' times. each loop creates one row.
            inner = []

            for k in range(z):          # Loop run 'z' times. each loop add values to rows.
                inner.append(value)     # Adds value into the row. This happens z times.
            block.append(inner)         # Adds completed rows into block
        arr.append(block)               # Adds the completed 2D block into 3D array.
    
    return arr 

print(create_array(2,2,3,5))

# Program: Write a program that defines a function create_list() to create and return a list which is an intersection
# of two lists passed to it.

# There are two ways do that program.
# First, method:

def create_list():
    
    l1 = [2,4,6,8,10,12,14,16,18,20]
    l2 = [4,8,12,16,20,24,28,32,36,40]

    l3 = set(l1) & set(l2)                  # '&' Opreator works only for "Set". not for list
    l3 = list(l3)

    return l3

print(create_list())

# Second Method, 

def create_list1():

    l5 = []

    l3 = [3,6,9,12,15,18,21,24,27,30]
    l4 = [5,10,15,20,25,30,35,40,45,50]

    for i in l3:
        if i in l4:
            l5.append(i)

    return l5

print(create_list1())


# Program: Write a program that defines a function sanitize_list() to remove all the duplicates entries from the list that
# it recieves.

def sanitize_list():

    l = [12,24,2,4,6,8,4,8,12,45,23,45]
    l = list(set(l))

    return l

print(sanitize_list())

