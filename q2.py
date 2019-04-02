# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

_NUM = int(input("Produce factorial for "))

def factorial(number):
    n = 1
    for i in range(1, number+1):
        n = n * i
    return n

if _NUM == 0:
    print(1)
elif _NUM < 0:
    print("INVALID INPUT: Negative numbers cannot produce a factorial")
else:
    print(factorial(_NUM))