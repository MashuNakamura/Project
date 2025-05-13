class Stack:
    # Data usage
    def __init__(self, size):
        self.size = size
        self.dataset = [None] * size
        self.top = - 1

    # Check if is full
    def is_full(self):
        return self.top == self.size - 1

    # Check if is empty
    def is_empty(self):
        return self.top == - 1

    # Function Push Data
    def push(self, data):
        if self.is_full():
            print("[INFO] Stack is Full !")
            return
        
        self.top += 1
        self.dataset[self.top] = data
        print(f"[INFO] Data {data} Successfully added")
            
    # Function Pop Data (Delete random data and return)
    def pop(self):
        if self.is_empty():
            print("[INFO] Stack is Empty")
            return
        
        data = self.dataset[self.top]
        self.dataset[self.top] = None
        self.top -= 1
        print(f"[INFO] Data {data} Successfully popped")
        return data

    # Function Peek Data
    def peek(self):
        if self.is_empty():
            print("[INFO] Stack is Empty")
            return
        
        print(f"[INFO] Top of the stack: {self.dataset[self.top]}")
        return self.dataset[self.top]
        
    # Function Clear Data and Reset from the start
    def clear(self):
        if self.is_empty():
            print("[INFO] Stack is Empty")
            return
        
        self.dataset = [None] * self.size
        self.top = - 1
        print(f"[INFO] Stack successfully cleared")