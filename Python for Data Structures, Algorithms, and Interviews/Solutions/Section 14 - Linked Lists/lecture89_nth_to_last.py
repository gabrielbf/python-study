'''
Section 14 - Lecture 90 - Linked List Nth to Last Node
Interview Problem Solution

meu_nth_to_last solução minha usando for para achar tamanho lista
nth_to_last solução do curso usando dois ponteiros
Node classe que modela um nodo da lista simplismente encadeada
'''


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


def meu_nth_to_last(n, head):
    # Edge cases
    if (not n) or (not head):
        return None

    cur = head
    size = 0
    while (cur.next_node):
        size += 1
        cur = cur.next_node

    jumps = size - n
    result = head
    if jumps > 1:
        while jumps:
            result = result.next_node
            jumps -= 1
    return result


def nth_to_last(n, head):
    # Edge cases
    if (not n) and (not head):
        return None

    # if n == 0:
    #     return last element
    right = head
    left = head

    for i in range(n):
        if not right.next_node:
            raise LookupError("n larger than list.")
        right = right.next_node

    while right.next_node:
        right = right.next_node
        left = left.next_node
    return left
