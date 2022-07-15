from unittest import result
from sympy import arg


def add(*args):
    result = 0
    for n in args:
        result += n
    return result