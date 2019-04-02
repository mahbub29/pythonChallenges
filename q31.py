# Define a function that can accept an integer number as input and print
# the "It is an even number" if the number is even, otherwise print "It is an odd number".


def even_odd(num):
    if int(num) % 2 == 0:
        return "It is an even number."
    else:
        return "It is an odd number."


print(even_odd(num=input()))
