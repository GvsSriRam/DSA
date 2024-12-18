class MinStack:

    def __init__(self):
        self.arr = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.update_min(val)

    def pop(self) -> None:
        ele = self.arr.pop()
        if ele == self.min:
            if self.arr:
                self.min = min(self.arr)
            else:
                self.min = float("inf")
        return ele

    def top(self) -> int:
        if self.arr:
            return self.arr[-1]
        return None

    def getMin(self) -> int:
        return self.min

    def update_min(self, val):
        self.min = min(self.min, val)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()