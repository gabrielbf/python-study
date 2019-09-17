'''
Section 12 - Lecture 63 - Unique Characters Strings

uni_char_counter solução minha usando collections.Counter
uni_char_list solução minha usando uma lista para controlar se char é novo
uni_char_set solução do curso usando one-liner com length de um set
uni_char solução do curso usando set como a minha solução com lista
'''
from collections import Counter


def uni_char_counter(s):

    # Edge cases
    if not s:
        return True
    if len(s) == 1:
        return True

    c = Counter(s)
    return (c.most_common(1)[0][1] <= 1)


def uni_char_list(s):
    # Edge Cases
    if not s:
        return True
    if len(s) == 1:
        return True

    viewed_chars = []
    for c in s:
        if c in viewed_chars:
            return False
        else:
            viewed_chars.append(c)
    return True


def uni_char_set(s):
    return len(set(s)) == len(s)


def uni_char(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True
