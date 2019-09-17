'''
Section 15 - Lecture 102 - Recursion Problem 3 - Fibonacci Sequence

fib_iter            Solução iterativa do curso
fib_rec             Solução recursiva do curso
fib_dyn             Solução recursiva com memoização do curso

fib_rec_meu         Minha solução recursiva
fib_rec_meu_errado  Minha solução que não está funcionando para zero
fib_dyn_meu         Minha solução recursiva com memoização
fib_iter_meu        Minha solução iterativa
'''


def fib_rec_meu(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec_meu(n-1) + fib_rec_meu(n-2)


def fib_rec(n):
    # Base case
    if n == 0 or n == 1:
        return n
    # Recursive case
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_rec_meu_errado(n):
    if n <= 2:
        # Retornando um para as posições 1 e 2
        # Não funciona quando n for zero
        return 1
    else:
        return fib_rec_meu_errado(n-1) + fib_rec_meu_errado(n-2)


# Cache
n = 10
cache = [None] * (n+1)


def fib_dyn(n, cache):
    # Base case
    if n == 0 or n == 1:
        return n

    # Check cache
    if cache[n] is not None:
        return cache[n]

    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)


# Assim o elemento que memoiza mantem o valor da posição e não do fatorial
# daquele número
memo = {0: 0, 1: 1}


def fib_dyn_meu(n, memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_dyn_meu(n-2, memo) + fib_dyn_meu(n-1, memo)
        return memo[n]


def fib_iter_meu(n):
    lista = [0, 1]
    # o zero não é um dos elementos da progressão segundo a solução do curso
    # como já tenho o primeiro valor ali (1),
    # preciso retirar um dos valores do range
    for i in range(n - 1):
        lista.append(lista[len(lista) - 2] + lista[len(lista) - 1])
    return lista.pop()


def fib_iter(n):
    # Set starting point
    a = 0
    b = 1

    # Follow algorithm
    for i in range(n):
        a, b = b, a + b

    return a
