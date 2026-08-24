from itertools import accumulate

data = [[x] for x in input().split()]
for value in accumulate(data):
    print(' '.join(value))
