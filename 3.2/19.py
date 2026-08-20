data = {}
for i in range(int(input())):
    line = input().replace(":", " ").replace(",", " ").split()
    toys = line[1:]
    name = line[0]
    for toy in set(toys):
        if toy not in data:
            data[toy] = 1
        else:
            data[toy] += 1
final = []
for toy, count in sorted(data.items()):
    if count == 1:
        print(toy)
