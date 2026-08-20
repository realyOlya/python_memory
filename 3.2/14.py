data = []
product = []
for i in range(int(input())):
    product.append(input())
for j in range(int(input())):
    name = input()
    count_products = int(input())
    count = 0
    for k in range(count_products):
        prod = input()
        if prod in product:
            count += 1
    if count == count_products:
        data.append(name)
data = sorted(data)
if len(data) != 0:
    for word in data:
        print(word)
else:
    print("Готовить нечего")
