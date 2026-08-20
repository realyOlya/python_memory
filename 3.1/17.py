line = input()
count = 1
for i in range(len(line) - 1):
    if line[i] == line[i + 1]:
        count += 1
    else:
        print(line[i], count)
        count = 1
print(line[-1], count)
