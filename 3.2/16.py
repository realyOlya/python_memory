final = set()
while (line := input()) != "":
    data = line.split()
    for i in range(1, len(data) - 1):
        if data[i] == "зайка":
            final.add(data[i - 1])
            final.add(data[i + 1])
    if data[0] == "зайка":
        final.add(data[1])
    if data[-1] == "зайка":
        final.add(data[-2])
for word in final:
    print(word)
