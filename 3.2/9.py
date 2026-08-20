data = {}
while (line := input()) != "":
    lis = line.split()
    for thing in lis:
        if thing not in data:
            data[thing] = 1
        else:
            data[thing] += 1
for thing, num in data.items():
    print(thing, num)
