x = float(input("Введите x: "))
y = float(input("Введите y: "))

if 0 <= x <= 6 and y <= -x + 6 and ((x <= 2 and y >= -2 * x + 4) or (x > 2 and y >= 0)):
    print(True)
else:
    print(False)
