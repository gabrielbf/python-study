'''
Section 14 - Implement a Singly Linked List

Não tem lecture mas é pra implementar como exercício
'''


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


# Implementing Singly Linked List

a = Node('a')
b = Node('b')
c = Node('c')

a.next_node = b
b.next_node = c
# c.next_node = None
