class Queue2Stack(object):

    def __init__(self):
        self.stack1 = []  # Front
        self.stack2 = []  # Rear

    def enqueue(self, item):
        self.stack1.append(item)
        self.stack2 = self.stack1.copy()
        self.stack2.reverse()

    def dequeue(self):
        ret = self.stack2.pop()
        self.stack1 = self.stack2.copy()
        self.stack1.reverse()
        return ret


class Queue2StackCurso(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
