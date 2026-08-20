data = {}
for i in range(int(input())):
    name = input()
    if name not in data:
        data[name] = 1
    else:
        data[name] += 1

count = 0
sort_data = dict(sorted(data.items()))
for name, k in data.items():
    if k > 1:
        print(f'{name} - {k}')
        count += 1
if count == 0:
    print("Однофамильцев нет")
