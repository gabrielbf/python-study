'''
Section 14 - Lecture 75 - Implement a Deque - Interview Problem
'''


class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    # Também pode ser return self.items == [] pois sei que items é lista
    def isEmpty(self):
        return not self.items
