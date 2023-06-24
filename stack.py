class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) 
print(stack.pop()) 
print(stack.is_empty())  
print(stack.pop())  
print(stack.is_empty())  
