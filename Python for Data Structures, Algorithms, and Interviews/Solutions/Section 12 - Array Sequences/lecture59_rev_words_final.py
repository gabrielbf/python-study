"""
Lecture 59 - Section 12 - Sentence Reversal Solutions

rev_words é a minha primeira solução.
Retorna o inverso do string de entrada

rev_words_solucao é a solução do curso.
Retorna lista com as palavras do string de entrada s.

final_output é função sugerida pelo curso para não usar reversed em
rev_words_solucao.
Retorna os elementos da lista l de entrada concatenados em um string.
"""

from collections import deque


def rev_words(s):
    if not s:
        return ""

    s_strip = s.strip()

    d = deque()
    palavra = []
    for char in s_strip:
        if not char.isspace():
            palavra.append(char)
        else:
            lista_aux = ''.join(palavra)
            d.append(lista_aux)
            palavra.clear()
    lista_aux = ''.join(palavra)
    d.append(lista_aux)
    palavra.clear()
    retorno = []
    for item in range(len(d)):
        retorno.append(d.pop())
    print(' '.join(retorno))


def rev_words_solucao(s):
    words = []
    length = len(s)
    space = [' ']

    i = 0
    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1
            words.append((s[word_start:i]))
        i += 1

    # return " ".join(reversed(words))
    return words


# Inverte
def final_output(l):

    d = deque(l)
    # retorno = ""
    retorno = []
    while d:
        retorno.append(d.pop())
    return " ".join(retorno)
