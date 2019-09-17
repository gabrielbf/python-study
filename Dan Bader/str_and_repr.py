"""
Class com implementação recomendada de __repr__()
https://dbader.org/blog/python-repr-vs-str
"""


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # chamar self.propriedades com flag !r para usar repr das propriedades
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')

    # def __repr__(self):
    #     return '{self.__class__.__name__}(' \
    #             '{self.color!r}, {self.mileage!r})'.format(self=self)
