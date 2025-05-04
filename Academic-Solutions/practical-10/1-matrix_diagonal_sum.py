n = int(input("Введите размер матрицы: "))

matrix = []
for i in range(n):
    row = list(map(int, input(f'Строка {i+1}/{n}: введите {n} числа (через пробел): ').split()))
    matrix.append(row)
    
diagonal_sum = 0
for i in range(n):
    element = matrix[i][n-1-i]
    if element % 5 == 0:
        diagonal_sum += element
        
print(f"Сумма элементов на диагонали, кратных 5: {diagonal_sum}")