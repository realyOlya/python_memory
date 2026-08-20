N = int(input())
M = int(input())
data1 = set()
data2 = set()
for _ in range(M + N):
    line = input()
    if line not in data1:
        data1.add(line)
    else:
        data2.add(line)
all_data = data1 ^ data2
if len(all_data) > 0:
    print(len(all_data))
else:
    print("Таких нет")
