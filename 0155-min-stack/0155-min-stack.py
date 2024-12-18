class MinStack:

    def __init__(self):
        self.arr = []
        self.prefix_min_arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.prefix_min_arr:
            self.prefix_min_arr.append(val)
        else:
            self.prefix_min_arr.append(min(val, self.prefix_min_arr[-1]))

    def pop(self) -> None:
        ele = self.arr.pop()
        self.prefix_min_arr.pop()
        return ele

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.prefix_min_arr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()