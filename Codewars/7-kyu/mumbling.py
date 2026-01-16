def accum(st):
    return '-'.join((st[i]*(i+1)).capitalize() for i in range(len(st)))

# Примеры:
assert accum("abcd") == "A-Bb-Ccc-Dddd"
assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
assert accum("cwAt") == "C-Ww-Aaa-Tttt"
