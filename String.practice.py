name = "My name is aditi rathi"

# Here, we are suppose to change 'n' to 'w'
# Since, the string in python is immutable. so we can't assign to a single character position of python.
# Does that means that we can't change them ??
# No, that's not case at all. python has what is called slicing.

name = name[:3]+"w" + name[4:]
print(name)


# Que 1: WAP that generates the following output from the string "Shenanigan".
# output: S h, an, enanigan, Shenan, seaia, Snin, Saa, ShenaniganType, ShenanWabbite

word = "Shenanigan"

print(word[0], word[1])  
print(word[4:6])
print(word[2:])
print(word[0: : 2])
print(word[0: :3])
print(word[0: :4])
print(word + "Type")
print(word + 'Wabbite')

# Que 2: WAP to convert the following string
#  Visit ykanetkar.com for online course in programming
# into
# Visit Ykanetkar.com For Onilne Course In Programing.

string = "Visit ykantkar.com for online course in programming"
print(string.title())


# Que 3: WAP to convert the following string
# Light travels faster than sound.This is why some pepole appear bright until you hear them speak.
# into
# Light travels faster than SOUND. This why some pepole appear bright until you hear them speak.

l = "Light travels faster than sound. This is why some pepole appear bright until you hear them speak."
print(l.replace("sound", "sound".upper()))

# Que 4: What will be the output of the following program?

s = "HumptyDumpty"
print(s.isalpha())   # Working of isalpha to check wheter all the characters in string is alphabetic

# Que 5: What is the porpose of a raw string?

row_str = "pyhton\nProgramming"
print(row_str)   # Use of raw string to make backslash\ behave like a normal character.

# Que 6: If we wish to work with an individual word in the following string, how will you separate them out:
#   "The difference between stupity and genius is that genius has its limit."

diff_str = "The difference between stupity and genius is that genius has limit."
diff_list = diff_str.split()
print(diff_list)
print(diff_list[5])  # Here, we want to suppose work with "genius" word


# Note: Python are iterables. because it goes through a string character by character using: for loop, list, indexing.

# Que 7: How will you eliminate spaces on either side of string '  Flanked by spaces on either side  '?

s = "  Flanked by spaces on either side   "
print(s.strip())