# Define a function with a generator which can iterate the numbers, which are divisible by 7,
# between a given range 0 and n.


def _NUM_PROCESSOR(n_max):
    i = 0
    while i <= n_max:
        if i % 7 == 0:
            yield i
        i += 1


n_max = int(input())
for item in _NUM_PROCESSOR(n_max):
    print(item)