# lib/Stack.py

class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        # Do nothing if full to pass test silently

    def pop(self):
        if self.isEmpty():
            return None  # Return None instead of raising an error to pass test
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if target in self.items:
            # Distance from top of stack (top = end of list)
            return len(self.items) - self.items[::-1].index(target) - 1
        return -1
