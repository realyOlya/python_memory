line = [int(x) for x in input().split("; ")]
line = sorted(set(line))
data = {}
for i in range(len(line)):
    coprimes = []
    for j in range(len(line)):
        if i == j:
            continue
        a, b = max(line[i], line[j]), min(line[i], line[j])
        while b != 0:
            a, b = b, a % b
        if a == 1:
            coprimes.append(str(line[j]))
    if coprimes:
        data[line[i]] = coprimes
for key in sorted(data):
    print(f"{key} - {', '.join(data[key])}")
