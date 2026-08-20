data = set()
for i in range(int(input())):
    line = input().split()
    data = data | set(line)
for word in data:
    print(word)
