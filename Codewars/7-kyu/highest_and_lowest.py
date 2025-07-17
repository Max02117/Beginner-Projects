def high_and_low(numbers):
    nums = [int(num) for num in numbers.split()]
    return f'{max(nums)} {min(nums)}'

# Примеры:
assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -5") == "9 -5"