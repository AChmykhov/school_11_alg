class Node:
    top = None

    def __init__(self, key, value, parent=None, left=None, right=None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def get(self, key):
        return self.search(key).value

    def search(self, key):
        if self.key == key:
            return self
        else:
            if self.key > key:
                return self.left.search(key)
            else:
                return self.right.search(key)

    def set(self, key, value):
        obj = self.search(key)
        obj.value = value
        return obj

    #
    # not done yet
    #
    def put(self, key, value, left=None, right=None):
        if key < self.key and self.left is None:
            self.left = Node(key, value, self, left, right)
        elif key > self.key and self.right is None:
            self.right = Node(key, value, self, left, right)
        else:
            if key < self.key:
                return self.left.put(key, value, left, right)

    def iterate(self):
        if self.left is None and self.right is None:
            return [self]
        elif self.left is None:
            return [self] + self.right.iterate()
        elif self.right is None:
            return self.left.iterate() + [self]
        else:
            return self.left.iterate() + [self] + self.right.iterate()

    def range(self, start_key, end_key):
        if start_key <= self.key <= end_key:
            if start_key == end_key == self.key:
                return [self]
            elif start_key == self.key:
                return [self] + self.right.range(start_key, end_key)
            elif self.key == end_key:
                return self.left.range()

            else:
        else:
            return []

