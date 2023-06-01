
class Repeat():
    def __init__(self, xs):
        self.xs = xs

    def __iter__(self):
        return self

    def __next__(self):

        return self.xs
