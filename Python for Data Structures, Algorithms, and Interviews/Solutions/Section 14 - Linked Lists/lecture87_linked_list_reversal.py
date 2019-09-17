'''
Section 14 - Lecture 87 - Linked List Reversal

Solução do curso

Node é classe que define os nodos da lista
    valeu é o valor do nodo
    next_node é o ponteiro pro próximo nodo
'''


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse(head):
    current = head
    prev_node = None
    next_node = None
    while current:
        next_node = current.next_node
        current.next_node = prev_node
        prev_node = current
        current = next_node
    return prev_node
