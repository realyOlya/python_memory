line1 = input().split(", ")
line2 = input().split(", ")
data = list(zip(line1, line2))
for name in data:
    print(f'{name[0]} - {name[1]}')
