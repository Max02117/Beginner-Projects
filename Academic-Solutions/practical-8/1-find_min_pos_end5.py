n = int(input('Введите количество элементов: '))
numbers = list(map(int, input(f'Введите {n} чисел (через пробел): ').split()))

if len(numbers) != n:
    print(f'Ошибка: ожидалось {n} элементов, получено {len(numbers)}')
    exit(1)
    
candidates = (num for num in numbers if num > 0 and num % 10 == 5)

if candidates:
    print(f'Минимальный подходящий элемент: {min(candidates)}')
else:
    print('Нет положительных чисел, оканчивающих на 5')