N = int(input())
M = int(input())
data1 = set()
data2 = set()
for _ in range(N):
    data1.add(input())
for _ in range(M):
    data2.add(input())
all_data = data1 & data2
if len(all_data) > 0:
    print(len(all_data))
else:
    print("Таких нет")
