# ------ RECURSION ------

# Repetitions: There are two ways to repeat a set of statements in a function:
# - By using while or for loop
# - By calling the function within itself.

# The first method is known as iteration, where as the second method is known as recursion.
# The functions that uses itreation, where as the second is known as recursion.


# ------- Recursive Function -------

# A Python function can be called from within its body. when we do so it is called recursive  function.

def fun():
    # some statements
    fun ()

# recursive call keeps calling the function again and again, leading to an infinte loop.
# A Provision must be made to gey outside this infinte recursive loop. This is done by making the recursive call either
# in if block or in else block as shown below:

def fun():
    #if condition:
        # some statemet
    #else:
        fun()


# ----- When to use Recursion ----

# Recursion is useful in 2 scenario:
# - When a problem can by breaking it down into similar sub-problems.
# - When a problem requries an unknown number of loops.


# Diffrence between FUNCTION vs RECURSION:

#    Function                                                                     # Recursion
# - A noraml block of code                                                        - A technique using a function
# - A function is a block of code that perfomes                                   - Recursion is a way of using a function
#   a specific task.                                                                where the function calls itself. 
# - It runs only when it is called.                                               - So, recursion is not different from a function
#                                                                                 - It is a technique used inside a function.


# Example of Recursion :

def factorial(n):
      if n == 1:
            return 1
      return n* factorial(n-1)

# Function calls itself.
# Has a base case

# Note: All recursive programs use functions, but not all functions are recursive.

# ------ Types of Recursion -----


# Head Recursion: In head recursion, the recursive call first, and the work is done after the function returns.

def fun(n):
      if n == 0:
            return
      fun(n-1)
      print(n)                     

# Output:  1
#          2
#          3


# Tail Recursion 

# In tail recursion, the recursive call is the last statement in the function.

def fun(n):
      if n== 0:
            return 
      print(n)
      fun(n-1)

# output:  3
#          2
#          1

# Recursion happens when a function calls itself.


# Program: If a positive integer is entered through the keyboard, write a recursive function to obtain the prime factors
#          of the number.


# An Important note: using if-else normally vs using in recursion function.

# -------- using in loops: ---------
# while condition:
#      if case1:
#            do A
#      else:
#            do B


#  ------- In recursion -------

# if case1:
#      do A
#      call function again

# else:
#      call function again differently

def factorize(n,i):
      if n == 1:
            return
      
      if n % i == 0:
            print(i)

            factorize(n // i, i)
      else:
            factorize(n, i + 1)

num = int(input("Enter your number: "))

factorize(num,2)
