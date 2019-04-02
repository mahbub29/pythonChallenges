# Write a program to generate and print another tuple whose values are even
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


t = (1,2,3,4,5,6,7,8,9,10)

def printTuple(t):
    tList = []
    for i in range(len(t)):
        if t[i] % 2 == 0:
            tList.append(t[i])
    print(tList)


printTuple(t)

