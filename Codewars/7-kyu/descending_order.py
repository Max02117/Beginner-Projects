def descending_order(num):
    digits = sorted(str(num), reverse=True)
    return int(''.join(digits))

# Примеры:
assert descending_order(42145) == 54421
assert descending_order(145263) == 654321
assert descending_order(123456789) == 987654321