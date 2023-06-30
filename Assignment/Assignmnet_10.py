class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()
            return item

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def get_min(self):
        if not self.is_empty():
            return self.min_stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


stack = MinStack()
stack.push(4)
stack.push(2)
stack.push(8)
stack.push(6)
stack.push(3)
print("Smallest Number:", stack.get_min())

