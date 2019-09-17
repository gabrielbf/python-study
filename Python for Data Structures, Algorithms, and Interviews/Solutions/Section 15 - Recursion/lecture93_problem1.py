'''
Section 15 - Lecture 93 - Problem 1

Minha solução igual a do curso
'''


def cum_sum(n):
    if n == 0:
        return 0
    else:
        return n + cum_sum(n - 1)
