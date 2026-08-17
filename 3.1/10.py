data = []
for i in range(int(input())):
    data.append(input())
main_name = input()
for line in data:
    if main_name.lower() in line.lower():
        print(line)
