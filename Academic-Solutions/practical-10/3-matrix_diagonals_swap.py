n = int(input('Введите размер матрицы: '))

matrix = []
for i in range(n):
    row = list(map(int, input(f'Строка {i+1}/{n}: Введите {n} чисел (через пробел): ').split()))
    if n != len(row):
        print(f'\nОшибка: ожидалось {n} элементов, получено {len(row)}')
        exit(1)
    matrix.append(row)
    
for i in range(n):
    matrix[i][i], matrix[i][-1-i] = matrix[i][-1-i], matrix[i][i]
    
print('\nИзмененная матрица:')
for row in matrix:
    print(' '.join(f'{num:4}' for num in row))