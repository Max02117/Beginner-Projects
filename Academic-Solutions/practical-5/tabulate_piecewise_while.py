import math

h = float(input("Введите шаг h: "))
x = -9.0

while x <= 9:
    if -9 <= x <= -6:
        y = 1 - (8/3) * (x + 9)
    elif -6 < x <= -1:
        y = -7 + (9/5) * (x + 6)
    elif -1 < x <= 2:
        y = 2 + (1/3) * (x + 1)
    elif 2 < x <= 7:
        y = 3
    elif 7 < x <= 9:
        y = 3 + math.sqrt(1 - (x - 8)**2)
    else:
        y = "не определён"
    print(f"x = {x:.2f}, y = {y:.2f}")
    x += h