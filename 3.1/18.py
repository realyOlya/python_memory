line = input().split()
data_num = []
data_do = []
for symbol in line:
    if symbol.isdigit():
        data_num.append(int(symbol))
    else:

        if symbol == "*":
            s = data_num[-2] * data_num[-1]
            del data_num[-2]
            del data_num[-1]
            data_num.append(s)
        elif symbol == "+":
            s = data_num[-2] + data_num[-1]
            del data_num[-2]
            del data_num[-1]
            data_num.append(s)
        else:
            s = data_num[-2] - data_num[-1]
            del data_num[-2]
            del data_num[-1]
            data_num.append(s)
print(data_num[0])
