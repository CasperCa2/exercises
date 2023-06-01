class PadZip:
    def __init__(self, item1, item2, padding=None):

        self.item1 = iter(item1)
        self.item2 = iter(item2)
        self.padding = padding

    def __iter__(self):
        return self

    def __next__(self):
        end_reached = 0

        try:
            item1 = next(self.item1)
        except StopIteration:
            item1 = self.padding
            end_reached += 1

        try:
            item2 = next(self.item2)
        except StopIteration:
            item2 = self.padding
            end_reached += 1

        if end_reached == 2:
            raise StopIteration()

        return (item1, item2)
