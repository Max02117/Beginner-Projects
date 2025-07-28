def filter_list(lst):
    return [x for x in lst if type(x) is int]

# Примеры:
assert filter_list([1,2,'a','b']) == [1,2]
assert filter_list([1,'a','b',0,15]) == [1,0,15]
assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123]