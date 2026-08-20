data = {}
for i in range(int(input())):
    name = input()
    if name not in data:
        data[name] = 1
    else:
        data[name] += 1

count = 0
for name, k in data.items():
    if k > 1:
        count += k
print(count)
