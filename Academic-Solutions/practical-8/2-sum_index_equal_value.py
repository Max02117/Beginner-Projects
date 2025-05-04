nums = list(map(int, input('Введите числа (через пробел): ')).split())
result = sum(num for i, num in enumerate(nums, start=1) if i == num)
print(f'Результат: {result}')