import random

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = - 1
        self.random_pos = random.randint(0, size - 1)
        self.count = 0
        self.is_first = False

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, data):
        if self.is_full():
            print("[INFO] Queue Full!")
            return
        
        elif self.is_first == False:
            self.front = self.rear = self.random_pos
            self.is_first = True
            
        self.rear = (self.rear + 1) % self.size  
        self.queue[self.rear] = data
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("[INFO] Queue Empty!")
            return

        self.front = (self.front + 1) % self.size
        removed = self.queue[self.front]
        self.queue[self.front] = None
        self.count -= 1
        return removed

    def display(self):
        visual = []

        for item in self.queue:
            if item is None:
                visual.append("None")
            else:
                visual.append(str(item))

        result = ", ".join(visual)
        print("[INFO] Queue  :", f"[{result}]")