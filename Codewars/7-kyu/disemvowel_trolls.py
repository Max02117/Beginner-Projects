def disemvowel(string_):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join(
        result
        for result in string_
        if result not in vowels
    )