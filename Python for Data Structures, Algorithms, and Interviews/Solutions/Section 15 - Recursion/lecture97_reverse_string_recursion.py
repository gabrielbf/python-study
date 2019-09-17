'''
Section 15 - Lecture 97 - Reverse a String

reverse_meu minha solução
'''


def reverse_meu(s):
    # Faltou edge case no meu
    if len(s) == 1:
        return s
    else:
        return s[len(s) - 1] + str(reverse_meu(s[:-1]))


def reverse(s):

    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]
