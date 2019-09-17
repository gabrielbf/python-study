'''
Section 14 - Lecture 73 - Implement a Stack Interview Problem
'''


class Stack(object):

    def __init__(self):
        self.items = []

    # Também pode ser self.items == [] por que se sabe o tipo self.items
    def isEmpty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]  # ou self.items(self.size())

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
