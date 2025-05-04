n, m = map(int, input('Введите размер массива (N M) через пробел: ').split())

matrix = []
for i in range(n):
    row = list(map(int, input(f'Строка {i+1}/{n}: Введите {m} чисел (через пробел): ').split()))
    if m != len(row):
        print(f'\nОшибка: ожидалось {m} элементов, получено {len(row)}')
        exit(1)
    matrix.append(row)
    
# Вычисление суммы первой и последней строки
border_sum = 0
if n > 0:
    border_sum += sum(matrix[0])
    if n > 1:
        border_sum += sum(matrix[-1])

# Вычисление боковых чисел внутренних строк
for row in matrix[1:-1]:
    if m > 0:
        border_sum += row[0]
        if m > 1:
            border_sum += row[-1]

print(f'\nСумма контурных элементов: {border_sum}')