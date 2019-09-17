'''
Section 15 - Lecture 93 - Problem 2

Minha solução ficou igual a do curso exceto pelo len(n) == 1 que
tem no curso e na minha não
'''


def sum_func(n):
    if n == 0:
        return 0

    if len(n) == 1:
        return n
    else:
        return (n % 10) + sum_func(n//10)
