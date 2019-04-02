# Write a function to compute 5/0 and use try/except to catch the exceptions.


def calc():
    return 5/0


try:
    calc()
except ZeroDivisionError:
    print("Cannot divide by zero.")


