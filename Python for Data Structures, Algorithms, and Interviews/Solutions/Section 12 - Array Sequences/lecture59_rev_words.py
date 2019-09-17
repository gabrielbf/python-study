def rev_words(s):
    # edge cases
    if not len(s):
        return ''

    s_strip = s.strip()
    if not len(s_strip):
        return ''

    word_list = s_strip.split()
    return ' '.join(reversed(word_list))


def rev_words_braco(s):
    making_word = False
    result = []  # deque aqui
    letters = []
    space = ' '

    for c in s:
        if c is space:
            if making_word:
                result.append(''.join(letters))
                letters.clear()
                making_word = False
        else:
            letters.append(c)
            making_word = True
