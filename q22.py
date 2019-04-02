# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

_INPUT = input()
_STRING_ARRAY = sorted(_INPUT.split(" "))
_STRING_OCCUR = []
n = 1

# print(_STRING_ARRAY)
# print(len(_STRING_ARRAY)-1)
# print(_STRING_ARRAY[0])
# print(_STRING_ARRAY[16])

for i in range(len(_STRING_ARRAY)-1):
    if _STRING_ARRAY[i] == _STRING_ARRAY[i-1]:
        n += 1
    elif _STRING_ARRAY[i] != _STRING_ARRAY[i-1]:
        _STRING_OCCUR.append((_STRING_ARRAY[i-1], n))
        n = 1
    else:
        n += 1

# print(sorted(_STRING_OCCUR))

for i in sorted(_STRING_OCCUR):
    print(i[0] + ":" + str(i[1]))


