'''
Section 14 - Lecture 86
Singly Linked List Cycle Check Interview Problem - SOLUTION

Node é classe que define um nodo das listas encadeadas

meu_cycle_check(Node)
É método que eu fiz para resolver o problema usando uma lista e teste de
pertence.

cycle_check(Node)
É o método do curso usando markers que traverse em velocidades diferentes.
'''


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


def meu_cycle_check(node):

    seen = []
    current = node
    while (current.next_node is not None):
        if current in seen:
            return False
        else:
            seen.append(current)
            current = current.next_node
    return True


def cycle_check(node):
    marker1 = node
    marker2 = node

    while (marker2 is not None) and (marker2.next_node is not None):
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True
    return False



a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a  # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z
