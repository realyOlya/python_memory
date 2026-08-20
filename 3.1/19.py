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
        elif symbol == "-":
            s = data_num[-2] - data_num[-1]
            del data_num[-2]
            del data_num[-1]
            data_num.append(s)
        elif symbol == "/":
            s = data_num[-2] // data_num[-1]
            del data_num[-2]
            del data_num[-1]
            data_num.append(s)
        elif symbol == "#":
            data_num.append(data_num[-1])
        elif symbol == "!":
            s = 1
            num = data_num[-1]
            del data_num[-1]
            for i in range(1, num + 1):
                s *= i
            data_num.append(s)
        elif symbol == "~":
            num = data_num[-1]
            del data_num[-1]
            if num > 0:
                data_num.append((0 - num))
            else:
                data_num.append(abs(num))
        elif symbol == "@":
            num1 = data_num[-1]
            num2 = data_num[-2]
            num3 = data_num[-3]
            del data_num[-3]
            del data_num[-2]
            del data_num[-1]
            data_num.append(num2)
            data_num.append(num1)
            data_num.append(num3)
print(data_num[0])
