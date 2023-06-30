class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_stack(stack):
    if stack.is_empty():
        return

    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
        return

    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.push(temp)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Original Stack:", stack.items)
reverse_stack(stack)
print("Reversed Stack:", stack.items)
