# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


_INPUT_STR = input()
_ARRAY_DIMS = [int(i) for i in _INPUT_STR.split(",")]
_ROWS = _ARRAY_DIMS[0]
_COLS = _ARRAY_DIMS[1]

_OUTPUT_ARRAY = [[0 for c in range(_COLS)] for r in range(_ROWS)]

for r in range(_ROWS):                  # for each row i.e. 0, 1, 2 ...
    for c in range(_COLS):              # for each column in row
        _OUTPUT_ARRAY[r][c] = r * c

print(_OUTPUT_ARRAY)