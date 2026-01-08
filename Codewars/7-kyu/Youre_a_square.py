def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

# Примеры:
assert is_square(-1) == False
assert is_square(0) == True
assert is_square(3) == False