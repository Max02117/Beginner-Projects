upper_triangle = list(map(int, input('Введите элементы верхнего треугольника (через пробел): ').split()))

# Определение размера матрицы
L = len(upper_triangle)
n = int((-1 + (1 + 8 * L)**0.5) // 2)
if n * (n + 1) // 2 != L:
    print('Ошибка: некорректная длина входного массива')
    exit(1)

# Построение матрицы
matrix = [[0] * n for _ in range(n)]

idx = 0
for i in range(n):
    for j in range(i, n):
        matrix[i][j] = matrix[j][i] = upper_triangle[idx]
        idx += 1
        
print("\nВосстановленная матрица:")
for row in matrix:
    print(" ".join(f"{num:4}" for num in row))