data = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for day in range(int(input())):
    today = data[day % 5]
    print(today)
