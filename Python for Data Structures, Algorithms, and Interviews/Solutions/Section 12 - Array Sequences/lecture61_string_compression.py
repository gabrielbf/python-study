"""
Lecture 61 - Section 12 - String Compression Solution

Recebe string e retorna a quantidade de cada caracter em um string
"""
from collections import Counter


def compress(s):
    # edge cases
    if not s:
        return s

    s_clean = s.strip()
    c = Counter(s_clean)
    element_counts = []
    for elem in c:
        element_counts.append(elem + str(c[elem]))
   
    return ''.join(element_counts)
