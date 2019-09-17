'''
Section 13 - Lecture 76
Balanced Parentheses Check - Solution

solution_minha é solução minha para o problema
isClosing é método auxiliar pra minha solução
balance_check é solução do curso
'''
def solution_minha(s):
    # Edge cases
    if not s:
        return False

    if (len(s) % 2) != 0:
        return False

    stack = []
    for c in s:
        if (len(stack) > 0) and (isClosing(c, stack[-1])):
            stack.pop()
        else:
            stack.append(c)

    return print(len(stack) == 0)


def isClosing(close, open):
    if open is '(':
        return close is ')'
    if open is '[':
        return close is ']'
    if open is '{':
        return close is '}'

# solution('[][]((()))')
# solution('(({[]()([])}))')
# solution('[(])')


def balance_check(s):

    # Edge Cases
    if not s:
        return False

    if (len(s) % 2) != 0:
        return False

    stack = []
    opening = set("(", "[", "{")
    matches = set(("(", ")"), ("[", "]"), ("{", "}"))
    for paren in s:
        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0
