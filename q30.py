# Define a function that can accept two strings as input and print the string
# with maximum length in console. If two strings have the same length, then
# the function should print all strings line by line.


def stringProcess(s1, s2):
    if len(s1) > len(s2):
        return s1
    elif len(s2) > len(s2):
        return s2
    else:
        return s1 + "\n" + s2


print(stringProcess(s1=input(), s2=input()))



