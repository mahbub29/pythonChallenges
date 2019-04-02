# Write a program which accepts a string as input to print "Yes" if the
# string is "yes" or "YES" or "Yes", otherwise print "No".


def yes(_in):
    if _in == "Yes" or _in == "yes" or _in == "YES":
        print("Yes")
    else:
        print("No")


yes(_in=input())
