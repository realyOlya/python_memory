data = {}
for i in range(int(input())):
    num1, num2 = [int(x) for x in input().split()]
    num1, num2 = num1 // 10, num2 // 10
    points = str(num1) + " " + str(num2)
    if points not in data:
        data[points] = 1
    else:
        data[points] += 1
max_count = 0
for count in data.values():
    if count > max_count:
        max_count = count
print(max_count)
