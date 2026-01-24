def is_isogram(string):
    return len(string) == len(set(string.lower()))

# Примеры:
assert is_isogram("Dermatoglyphics") == True
assert is_isogram("aba") == False
assert is_isogram("moOse") == False
