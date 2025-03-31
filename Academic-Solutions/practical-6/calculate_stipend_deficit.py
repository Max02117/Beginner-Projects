A = float(input("Введите степендию: "))
B = float(input("Введите начальныые расходы: "))

if B <= A:
    print("Ошибка: Расходы должны быть больше степендии.")
    exit()

total = 0
current = B

for _ in range(10):
    deficit = A - B
    total += current
    current *= 1.03

print("Нужно попросить:", round(total - 10*A), "рублей.")