class node:
    numMade = 0

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.ID = node.numMade
        node.numMade += 1

    def __str__(self): return str(self.data)

    def set_next(self, node): self.next = node

    def get_next(self): return self.next

    def set_prev(self, node): self.prev = node

    def get_prev(self): return self.prev

    def get_data(self): return self.data
