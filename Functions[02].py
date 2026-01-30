# ====== Functions ========

# Program: Write a program to recive three intergers from keyborad and get thier sum and product calculated through a
# User-defined function cal_sum_prod().

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter third Number: "))

def cal_sum_prod(x,y,z):
    sum = x+y+z
    prod = x*y*z

    print("Product of Numbers:", prod)
    print("Sum of Numbers:", sum)

cal_sum_prod(num1, num2, num3)


# Program: Write a Python program that accepts a hypen-seprated sequence of words as input and calls a function convert()
# which convert it into a hyphen-seprated sequence after sorting them alphabatically. For example, if the input string is

# "here-come-the-dots-followed-by-dashes"
# then, the coverted string should be
# "by-come-dashes-dots-followed-here-the"

# "Hypen-seprated sequence of words" mean is words are joined using - (hyphen)

string = set("here-come-the-dots-followed-by-dashes")    # Set remove duplicates. and print the character individually.
# So, here are not going to use set().

def convert(s):
    words = s.split("-")        # split("-") : Breaks string into words.
    words.sort()                # sort() : Arrange words alphabetically

    return "-".join(words)     # Join words back using hypen.

s1 = input("Enter your string: ")

print(convert(s1))

# Note: Using split() without anything. 
#       - Default split() works on spaces.
#       - Your string has no spaces, only hypens.
#       - So the whole string becomes on single element.


# Program: Write a Python function to create and return a list containing tuples of the form (x, x^2, x^3) for all x between 1 and
# 20 (both include).

def values(x):

    l = []
    
    for i in range(1,21):
        a = i
        b = i**2
        c = i**3

        l.append((a,b,c))

    print(l)

print(values(2))


# Program: A plaindrome is a word or phrase which reads the same in both directions. Given below are some palindrome strings.
# deed
# level
# Malayalam
# Rats live on no evil star
# Murder for a jar of red rum

# Write a program that defines a function isplaindrome() which checks wheter a given string is a plaindrome or not. Ignore spaces
# and case mismatch while checking for plaindrome.


def isplaindrome(s):
    
    s = s.lower()
    s = s.replace(" ", "")

    if s[::-1] == s:
        print("This is a plaindrome")

    else:
        print("This is not a plaindrome")

str1 = input("Enter your string : ")
(isplaindrome(str1))


# Program: Write a program that defines a function convert() that recieves a string containg a sequence of whitespace seprated
# words and return a string after removing all duplicates words and shorting them aplhanumerically.

# Whitespace :- Whitespace means characters that create empty space in text. They are used to separate words or move text to a
# new line, but they are not visible.

# example: 
text = "Hello\tworld\nPython"             # Output: Hello    world
print(text)                                #        Pyhton


def convert(s):
    s = s.split()                        # Split() is used to convert the whole sentence into a single-single words. " ", " ",....                         
    s = sorted(s)                        # sorted() is used make order. according to alphabet and numercial value.

    s = list(set(s))                     # set is used to remove all the duplicates from the sentence.
    result = " ".join(s)                 # " ".join() is used to join the words with one time space.

    print(result)

convert("Sakshi was a singer because her mother was a singer, and sakhi\'s mother was a singer because her father was a singer")


# Program: Write a Program that defines a function count_alphabets_digits() that accepts a string and calculates the number
# of alphabets and digits in it. it should return thesse values as a dictionary. Call this function for some sample strings.

def count_alphabets_digits(s):
    d = {}

    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    print(d)

str1 = input("Enter Your string with digits: ")

count_alphabets_digits(str1)


# Program: Write a Program that defines a function called frequency() which computes the frequency of words present in a string
# passed to it. The frequencies should be returned in sorted order by words in the string.

def frequency(s):

    f = {}
    s = s.split()

    for i in s:
        if i in f:
            f[i] += 1

        else:
            f[i] = 1

    print(f)

str2 = input("Enter your String: ")
frequency(str2)


# Program: Write a Program that defines a function count_alphabets_digit() that accepts a string and calculates the number
# of alphabets and digits in it. it should return thesse values as a dictionary. Call this function for some sample strings.

def count_alphabets_digit(s):

    digits = 0
    alphabets = 0

    for ch in s:
        if ch.isalpha():
            alphabets += 1
        
        elif ch.isdigit():
            digits += 1

        else:
            pass

    print("Total Number of Digitis: ", digits)
    print("Total Number of Alphabets: ", alphabets)

s3 = input("Enter your String: ")

count_alphabets_digit(s3)