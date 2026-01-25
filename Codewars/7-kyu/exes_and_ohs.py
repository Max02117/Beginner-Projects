def xo(s):
    return s.lower().count('x') == s.lower().count('o')

# Примеры:
assert xo("ooxx") == True
assert xo("xooxx") == False
assert xo("ooxXm") == True
