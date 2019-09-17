"""
Python Iterators: A Step-By-Step Introduction – dbader.org
https://dbader.org/blog/python-iterators
"""


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value
