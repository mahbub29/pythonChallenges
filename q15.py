# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106


_INPUT_STR = "a+aa+aaa+aaaa"

_NUM_IN = input()

# ***

for char in _INPUT_STR:
    if char == "a":
        _INPUT_STR = _INPUT_STR.replace(char, _NUM_IN)

print(eval(_INPUT_STR))



# ***  import operator
#      d = {"a": _NUM_IN, "+": "+"}
#      for char in _INPUT_STR:
#      print(eval(_INPUT_STR.replace(char, d[char])))