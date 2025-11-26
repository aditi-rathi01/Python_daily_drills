# Question 1:
#  WAP that swaps the values of variable a and b. you are not allowed to use a third variable. you are not allowed to 
#      perfom arithmetic on a and b
# Ans.
a = 10
b = 20
a,b = b,a
print(a)
print(b)


# Question 2: 
# WAP that make use of trignometric functions avialable in math module.
# Ans.
import math
angle = 30
radian_value = math.radians(angle)
print("sin value= ", math.sin(radian_value))

# Question 3:
# WAP that genrates 5 random numbers in the range in the range 10 to 50.use a seed value of 6.

import random
random.seed(6)
print("random number between 10 to 50:")
for i in range(5):
    print(random.randint(10,50))


# Que 4: Use trunc(), floor() and ceil() for numbers -2.8, -0.5, 0.2, 1.5 and 2.9 to understand the differnce between these functions

print(" trunc(): Removes the decimal part")
print("floor(): Return the largest integer.")
print("ceil(): Return dthe smallest integer.")

import math
num = [-2.8, -0.5, 0.2, 1.5, 2.9]
for n in num:
    print("trunc:", math.trunc(n))
    print("floor:", math.floor(n))
    print("ceil:", math.ceil(n))

# Que 5: Assume a suitable value for temparature of a city in fahrenheit degrees. WAP to covert this temparature into centigrate.

print("formula: ", "C = 5/9(F-32)")
temp_fahr = 76 # 76 F
temp_cent = (temp_fahr - 32)*5/9
print("temp before in fahrenhiet:",temp_fahr)
print("temp after in centigrate:",temp_cent)

# Que 6: Print imaginary part of 2+3j.

com_num = 2+3j
print(com_num.imag)

# Que 7: Obtain conjucate of 4+2j.

z = 4+2j
print(z.conjugate())

# === Note ===
print("Note: In finding Imaginary part, we didn't use (). because it is attribute. No, parentheses is requried. we are not calling.")
print("Note: Conjucate is a function. so, must called by parenthesis().")

# Que 8: Convert a float value 4.33 into a numeric string.

f_value = 4.33
s_value = str(f_value)
print(s_value)


# Que 9: obatain integer quotient and remainder while dividing 29 with 5

q = 29//5    # To obtain integer quotient 
r = 29 % 5   # To obtain remaimder

print("quotient = ", q)
print("remainder = ", r)


# Obtain 4 from 3.556.

import math
n = 3.556
print(math.ceil(n))     # use ceil function. ceil() gives the next highest integer