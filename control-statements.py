# ==== control statment ====

# program 1: WAP to check whether a given number is in between 1 to 10.

num = int(input("Enter your number:"))

if (num>=1 and num<=10):
   print("Number", num, "is between 1 to 10")

else:
    print("number", num, "is not between 1 to 10")


# Program 2: WAP to check if a given number is zero, positive or negative.

num1 = int(input("enter your number"))
if(num1>0):
    print("Number is positive")

elif(num1<0):
    print("number is negative")
else:
    print("number is zero")


# ---- While Loop ----

# program 1: Write a program to display number from 1 to 10 using while loop.

i = 1
while(i<=10):
    print(i)
    i +=1

# program 2: WAP to display even numbers between 100 to 200.

x = 100
while x>=100 and x<=200:
    #print(x)
    x+=2

# program 3: WAP in which user enter two numbers 'm' and 'n'. 'm' is minimum and 'n' is maximum limit. and we need to find all the 
#  even number between 'm' and 'n'.

m = int(input("enter minimum limit:"))
n = int(input("enter maximum limit:"))
a = m
while a<=n:
   if a%2 ==0:
        print(a)
        a +=1


# --- For loop----

# program 1: WAP to display each character from a string using sequence index.

sting = "Hello Python"
n = len(sting)
for i in range(n):
    print(sting[i])


# program 2: WAP to display odd numbers from 1 to 10 using range() object.

for i in range(11):
    if i % 2!=0:
        print(i)

# program 3: WAP to display numbers from 10 to 1 in descending order. using a range function.
for i in range(10,0,-1):
    print(i)

# program 4: WAP to display and find the sum of a list of numbers using for loop.

list = [10,20,30,40,50]
sum = 0
for i in list:
    print(i)

    sum += i
print("sum = ", sum)

# WAP to displays stars in right angled triangular form using nested loop.
for i in range(1,11):
    for j in range(1, i+1):
        print("*", end="")
    print() 

# Program 5: WAP to display numbers from 10 to 6 and break the loop when the number about to display is 5.

i = 10
while i>=1:
     print(i)
     i -= 1
     if x==5:
        break   # Using 'BREAK' statment
print("out of the loop")

# Program 6: WAP to display numbers from 1 to 5 using continue statement.

x = 0
while x<=10:
    
    x +=1
    if x>5:
        continue
    print(x)
print("out of loop")   # Using 'Countinue' Statment.


# Program 7: WAP to retrieve only negative numbers from a list of numbers.

num = [1,34,-22,43,-55,-99, 10, 25]
for i in num:
    if i>=0:
        pass        # Using 'Pass' statment.
    else:
        print(i)

# Program 8: WAP to display prime number series

max = int(input("upto, what number:"))
for n in range(2,max+1):
    for i in range(2,n):
        if n % i ==0:
            break
    else:
        print(n)