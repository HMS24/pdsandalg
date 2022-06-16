"""https://leetcode.com/problems/implement-stack-using-queues/
"""

# Approach1 deque
"""

"""
from collections import deque


class MyStack:

    def __init__(self):
        self._queue = deque()
        
    def push(self, x: int) -> None:
        self._queue.append(x)
        for _ in range(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return len(self._queue) == 0