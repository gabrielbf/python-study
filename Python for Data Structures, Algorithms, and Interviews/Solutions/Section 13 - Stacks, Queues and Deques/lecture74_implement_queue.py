'''
Section 13 - Lecture 74 - Implement a Queue
'''


class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    # também pode ser return self.items == [] por que sei que items é lista
    def isEmpty(self):
        return not self.items

    # Em ordem trocada pode ser assim:
    # def enqueue(self, item):
    #     self.items.insert(0, item)

    # def dequeue(self):
    #     return self.items.pop()
