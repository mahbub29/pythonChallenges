# Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

_LINE_SEQ = []

while True:
    _INPUT_LINE = input()
    if _INPUT_LINE:
        _LINE_SEQ.append(_INPUT_LINE.upper())
    else:
        break

print("\n".join(_LINE_SEQ))