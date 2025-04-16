import random

class CircularStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = random.randint(0, size - 1)
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0
    
    def display_stack(self):
        print(f"Stack : {self.stack}")
        
    def display_count(self):
        print(f"Count : {self.count}")

    def push(self, data):
        if self.is_full():
            print("Stack is Full")
            return

        if self.count == 0:
            idx = self.top
            self.stack[idx] = data
            self.count += 1
            self.top = (self.top + 1) % self.size
            print(f"Added first data at random index : {idx}, value : {data}")
        else:
            idx = self.top
            self.stack[idx] = data
            self.count += 1
            self.top = (self.top + 1) % self.size
            print(f"Added data at index : {idx}, value : {data}")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return

        idx = (self.top - 1 + self.size) % self.size
        popped = self.stack[idx]
        self.stack[idx] = None
        self.count -= 1
        self.top = idx
        print(f"Popped data at index: {idx}, value: {popped}")
        return popped