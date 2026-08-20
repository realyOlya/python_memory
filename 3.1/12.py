data = []
for _ in range(int(input())):
    data.append(int(input()))
p = int(input())
for line in data:
    print(line ** p)
