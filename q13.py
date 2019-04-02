# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

_INPUT_STR = input()

_LETTERS = 0
_DIGITS = 0

for i in _INPUT_STR:
    if i.isalpha():
        _LETTERS += 1
    elif i.isdigit():
        _DIGITS += 1
    else:
        pass

print("LETTERS " + str(_LETTERS) + "\n" + "DIGITS " + str(_DIGITS))



# OR YOU CAN DO THE FOLLOWING:
#
#
# d={"DIGITS":0, "LETTERS":0}
# for i in _INPUT_STR:
#     if i.isdigit():
#         d["DIGITS"] += 1
#     elif i.isalpha():
#         d["LETTERS"] += 1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])