x = float (input("Введите x: "))

if x > 3:
    f = 1.2 * x**2 - 3*x - 9
else:
    f = 12.1 / (2*x**2 + 1)
print("F(x) = ", round(f, 3))
