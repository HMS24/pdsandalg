class Queue():
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return f"{self.queue}"

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def enqueue(self, x):
        self.stack.append(x)

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]