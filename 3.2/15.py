data = [int(x) for x in input().split(" ")]
data_out = []
k_digits = 0
k_units = 0
k_zeros = 0

for num in data:
    num = bin(num)[2:]
    k_digits = len(num)
    k_units = num.count("1")
    k_zeros = num.count("0")
    data_out.append({"digits": k_digits, "units": k_units, "zeros": k_zeros})
print(data_out)
