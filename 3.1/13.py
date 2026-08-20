data = [int(x) for x in input().split()]
p = int(input())
for line in data:
    print(line ** p, end=' ')
