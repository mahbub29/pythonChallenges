# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position after
# a sequence of movement and original point. If the distance is a float,
# then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2


XY = [0,0]
_COMMAND_ARRAY = []

def _EXECUTE_COMMANDS(_COMMAND_ARRAY, XY):
    for command in _COMMAND_ARRAY:
        if command[0] == "UP" or command[0] == "U":
            XY[1] += int(command[1])
        elif command[0] == "DOWN" or command[0] == "D":
            XY[1] -= int(command[1])
        elif command[0] == "LEFT" or command[0] == "L":
            XY[0] -= int(command[1])
        elif command[0] == "RIGHT" or command[0] == "R":
            XY[0] += int(command[1])
        else:
            print("There has been and error")


def _CALC_DIST(XY):
    import math
    dist = math.sqrt(XY[0]**2 + XY[1]**2)
    return dist


while True:
    _INPUT = input()
    if not _INPUT:
        break
    else:
        _COMMAND_ARRAY.append(tuple(_INPUT.split(" ")))

print(_COMMAND_ARRAY)

_EXECUTE_COMMANDS(_COMMAND_ARRAY, XY)

print(XY)

dist = _CALC_DIST(XY)

print(dist)
print(round(dist))

