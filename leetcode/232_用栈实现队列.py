class MyQueue:
    def __init__(self):
        self.stk = []
        self.tmp = []

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        while len(self.stk) > 1:
            self.tmp.append(self.stk[-1])
            self.stk.pop(-1)
        x = self.stk[-1]
        self.stk.pop(-1)
        while len(self.tmp):
            self.stk.append(self.tmp[-1])
            self.tmp.pop(-1)
        return x

    def peek(self) -> int:
        while len(self.stk) > 1:
            self.tmp.append(self.stk[-1])
            self.stk.pop(-1)
        x = self.stk[-1]
        while len(self.tmp):
            self.stk.append(self.tmp[-1])
            self.tmp.pop(-1)
        return x

    def empty(self) -> bool:
        return len(self.stk) == 0


queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
queue.pop()
print(queue.empty())
