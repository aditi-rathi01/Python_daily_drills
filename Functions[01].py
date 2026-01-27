# ====== Functions ========

# What are Functions?

# Python function is a block of code that perfomes a specific and well defined task. 

# There are two types of Python functions:
# a.) Built-in functions - Ex. len(), sorted(), min(), max() etc.
# b.) User-defined functions.

# Given below is an example of user-defined function. 

def fun():
    print("Hii, Everyone My Name is Aditi Rathi")

fun()

# A Function can be redefined. While calling the function its latest defination will be called.

# Function defination can be nested. When we do so, the inner function is able to access the variable of outer function.
# The Outer function must be called for the inner function to execute.

def outer():
    print("This is Outer Function:")

    def inner():
        print("This is inner function")
    
    inner()
outer()


# -------- Communication with Functions: ---------

# Communication with function means how function talks to each other and exchange data.

# They Communicate using:
# 1. Arguments(input)
# 2. Return values(outputs)

# The Way to pass values to a function and return value from it is shown below:

def cal_sum(x,y,z):
    return x+y+z


# Pass 10,20,30 to cal_sum(), collect value returned by it.
print(cal_sum(2,3,4))

# Pass a,b,c to cal_sum(), collect value returned by it.

a,b,c = 3,4,5
print(cal_sum(a,b,c))


# Return statments control and value from a function. returns without an expression returns None.

# To return multiple values from functions we can put them into a list/tuple/set/dictionary and then return it.


# Types of Arguments
# Argguments in Python function can be 4 types:
# a.) Positional Arguments
# b.) Keyward Arguments
# c.) Variable-length Positional Arguments
# d.) Variable-length keyward Arguments

# Positional and keywards arguments are often called 'requried' arguments, whereas, variable-length arguments are called 
# optianl arguments

# Positional Arguments: When you call a function, the first value goes to first varibale, the second value goes to the
# second varibale.   (Position decides which value goes where.)

# Example:
def fun(i,j,k):
    print(i+j)
    print(k.upper())

print(fun(3,4,"aditi"))
# But print(fun(4,"aditi", 3)) gives error.


#-------- Keyward Arguments:-------
# Keywards arguments mean you tell Pyhton the name of the variable.

# Example:
def info(name, age):
    print(name, age)

print(info(name= "adtit", age= 23 ))


# --------*Args -------

# *args: You don't need to know in advance how many values will be passed.

# Example 1: Adding Numbers.
def add(*args):
    print(args)

print(add(1,24,664,222,55))

# Note: Python collects all the values into a tuple called args.

# Example 2:
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(2,5,10))


# Example 3: 
def wel(*names):
    for name in names:
        print("Hii", name)

print(wel("Aditi", "Sherya", "Archna"))


# Sometimes number of postional arguments to be passed to a function is not certain. In such case, variable length positional
# argumnets can be received using *args.

