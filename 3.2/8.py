data = {}
for i in range(int(input())):
    line = input().split()
    name = line[0]
    porridges = line[1:]
    for porridge in porridges:
        if porridge not in data:
            data[porridge] = [name]
        else:
            data[porridge].append(name)
need_porridge = input()
flag = False
for porridge, name in data.items():
    if porridge == need_porridge:
        for word in sorted(name):
            print(word)
            flag = True

if not flag:
    print("Таких нет")
