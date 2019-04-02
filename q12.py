# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.


_OUTPUT_SEQ = []

for i in range(1000, 3001):
    for s in str(i):
        if int(s) % 2 != 0:
            break
    else:
        _OUTPUT_SEQ.append(i)

print(",".join([str(i) for i in _OUTPUT_SEQ]))
print(len(_OUTPUT_SEQ))