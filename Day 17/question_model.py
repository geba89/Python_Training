from pydoc import TextRepr

from matplotlib.pyplot import text


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
    