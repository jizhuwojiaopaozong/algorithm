from collections import deque


class MyStack:
    def __init__(self):
        self.deque = deque()

    def push(self, x: int) -> None:
        n = len(self.deque)
        self.deque.append(x)
        while n:
            self.deque.append(self.deque.popleft())
            n -= 1

    def pop(self) -> int:
        x = self.deque.popleft()
        return x

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        return len(self.deque) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
stack.pop()
print(stack.empty())
