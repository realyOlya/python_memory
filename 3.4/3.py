from itertools import count

line = [float(x) for x in input().split()]
for num in count(line[0], line[-1]):
    if num > line[1]:
        break
    print(f'{num:.2f}')
