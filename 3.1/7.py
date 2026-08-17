for i in range(int(input())):
    word = input()
    num = word.find("зайка")
    if num != -1:
        print(num + 1)
    else:
        print("Заек нет =(")
