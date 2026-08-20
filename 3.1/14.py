data = [int(x) for x in input().split()]
result = data[0]
for i in range(1, len(data)):
    a, b = result, data[i]
    while b != 0:
        a, b = b, a % b
    result = a

print(result)
