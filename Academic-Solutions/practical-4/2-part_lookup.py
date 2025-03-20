number = int(input("Введите номер детали: "))

details = {
    1: "шуруп",
    2: "гайка",
    3: "винт",
    4: "гвоздь",
    5: "болт"
}

if number in details:
    print("Название детали:", details[number])
else:
    print("Ошибка: детали с таким номером нет.")
