L = int(input()) - 3
data = []
for i in range(int(input())):
    data.append(input())
for line in data:
    if len(line) < L:
        print(line)
        L -= len(line)
    else:
        print(line[:L] + "...")
        exit()
