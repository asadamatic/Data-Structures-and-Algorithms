
class Stack:

    def __init__(self):

        self.stack = []

    def push(self, item):

        self.stack.append(item)

    def pop(self):

        return self.stack.pop()

    def peak(self):

        if not self.is_empty():

            return self.stack[-1]

    def is_empty(self):

        return len(self.stack) == 0

    def print(self):

        for item in self.stack:

            print(item)

stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push("2")
stack.push(3)

stack.print()

stack.pop()

stack.print()

print(stack.peak())

print(stack.is_empty())