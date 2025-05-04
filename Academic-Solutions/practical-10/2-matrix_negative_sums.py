m, n = map(int, input('Введите размер массива (M, N) через пробел: ').split())

matrix = []
for i in range(m):
    row = list(map(int, input(f'Строка {i+1}/{m}: Введите {n} чисел (через пробел): ').split()))
    matrix.append(row[:m])
    
sums = []
for row in matrix:
    negative_sum = sum(num for num in row if num < 0)
    sums.append(negative_sum)
    
print(f'\nСумма отрицательных чисел: {sums}')