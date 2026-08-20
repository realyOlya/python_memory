data = {}
while (line := input()) != "":
    name1, name2 = line.split()
    if name1 not in data:
        data[name1] = set()
    data[name1].add(name2)
    if name2 not in data:
        data[name2] = set()
    data[name2].add(name1)

for key in sorted(data):
    friends = set()
    for name in data[key]:
        friends |= data[name]
    friends -= data[key]
    friends -= {key}
    result = ", ".join(sorted(friends))
    print(f"{key}: {result}")