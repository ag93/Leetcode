class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        self.cnt = 0
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.cnt == 0:
            self.min.append(x)
        else:
            var = self.min[self.cnt-1]
            if var > x:
                self.min.append(x)
            else:
                self.min.append(var)
        self.cnt += 1
        

    def pop(self) -> None:
        self.stack.pop(self.cnt-1)
        self.min.pop(self.cnt-1)
        self.cnt -= 1

    def top(self) -> int:
        return self.stack[self.cnt-1]

    def getMin(self) -> int:
        return self.min[self.cnt-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()