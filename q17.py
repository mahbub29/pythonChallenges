# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500


_BALANCE = 0

while True:
    _IN = input()
    if not _IN:
        break
    _IN_VALUES = _IN.split(" ")
    if _IN_VALUES[0] == "D":
        _BALANCE += int(_IN_VALUES[1])
    elif _IN_VALUES[0] == "W":
        _BALANCE -= int(_IN_VALUES[1])
    else:
        pass

print("BALANCE £" + str(_BALANCE))
