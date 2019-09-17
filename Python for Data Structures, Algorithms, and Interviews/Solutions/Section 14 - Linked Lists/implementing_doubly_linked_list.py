'''
Section 14 - Implement a Doubly Linked List

Não tem lecture mas é dito no curso para implementar como exercício
Lembrar que lista precisa ter Sentinels nas pontas para algoritmos funcinarem
'''


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Implementing Doubly Linked List
a = Node('a')
b = Node('b')
c = Node('c')

a.next = b
a.prev = None
b.next = c
b.prev = a
c.next = None
c.prev = b
