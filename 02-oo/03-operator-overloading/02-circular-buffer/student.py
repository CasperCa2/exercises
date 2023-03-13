class CircularBuffer:

    def __init__(self, n, buffer):
        assert len(buffer) <= n, "fout"
        buffer = []
        self.maximum_size = n
        self.buffer = buffer

    def __add__(self, item):
        if len(self.buffer) > self.maximum_size:
            self.buffer.__removetitem__(0)
            self.buffer += item

    def __len__(buffer):
        return len(buffer)

    def __removetitem__(self, index):
        self.buffer.remove(index)
