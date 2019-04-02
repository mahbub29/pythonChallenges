# Define a function which can generate a list where the values are square of
# numbers between 1 and 20 (both included). Then the function needs to print
# the first 5 elements in the list.


def squareList():
    squares = []
    for i in range(1, 21):
        squares.append(i**2)
    print(squares[:5])


squareList()
