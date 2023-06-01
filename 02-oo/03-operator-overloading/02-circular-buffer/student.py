class CircularBuffer:
    def __init__(self, n):
        self.max = n
        self.circularbuffer = []

    def __len__(self):
        return len(self.circularbuffer)

    def __getitem__(self, index):
        return self.circularbuffer[index]

    def add(self, item):
        if len(self.circularbuffer) >= self.max:
            self.circularbuffer.pop(0)
        self.circularbuffer.append(item)
