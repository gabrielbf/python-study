'''
Section 15 - Lecture 93 - Problem 3

word_split_meu é minha tentativa de solução pro problema
word_split é solução do problema do curso
'''


def word_split_meu(phrase, list_of_words):
    if phrase and list_of_words:
        if phrase.count(list_of_words[0]) > 0:
            return ''.join([list_of_words[0],
                            word_split(phrase.replace(list_of_words[0], '', 1),
                            list_of_words[1:])])
    else:
        return ''


def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output
