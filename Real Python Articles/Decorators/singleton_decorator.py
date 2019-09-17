"""
Function Decorator que recebe uma classe e a torna um singleton
"""
import functools


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()

id(first_one)
id(another_one)
first_one is another_one
