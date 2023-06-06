# Enter your code here:


class StorageDevice():

    def __init__(self, block_count, block_size):
        self.blockcount = block_count
        self.blocksize = block_size

    def block_count(self):
        return self.blockcount

    def block_size(self):
        return self.blocksize
