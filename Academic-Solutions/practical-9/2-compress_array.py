arr = list(map(int, input("Введите элементы массива (через пробел): ").split()))
compressed = [num for num in arr if num != 0]

print("Сжатый массив: ", compressed)