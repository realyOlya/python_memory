data = {}
for i in range(int(input())):
    data[input()] = 1
for j in range(int(input())):
    for k in range(int(input())):
        line = input()
        if line in data:
            data[line] -= 1
data = dict(sorted(data.items()))
flag = False
for line, k in data.items():
    if k == 1:
        print(line)
        flag = True
if not flag:
    print("Готовить нечего")
