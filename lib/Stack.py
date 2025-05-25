class Stack:

    def __init__(self, items=None, limit=100):
        self.stack = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.full():
            raise OverflowError("Stack is full")
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def full(self):
        return len(self.stack) >= self.limit

    def search(self, target):
        try:
            # Distance from top is reverse index
            return len(self.stack) - self.stack[::-1].index(target) - 1
        except ValueError:
            return -1
