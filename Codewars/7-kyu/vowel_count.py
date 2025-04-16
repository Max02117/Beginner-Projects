def get_count(sentence):
    return sum(1 for c in sentence if c in "aeiou")