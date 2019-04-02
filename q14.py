# Write a program that accepts a sentence and calculate the
# number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

_IN = input()
_UPPER = 0
_LOWER = 0

for char in _IN:
    if char.isupper() == True:
        _UPPER += 1
    elif char.islower() == True:
        _LOWER += 1
    else:
        pass

print("UPPER CASE", _UPPER)
print("LOWER CASE", _LOWER)