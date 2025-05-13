class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, data):
        if self.is_full():
            print("[INFO] Queue is Full!")
            return
        
        self.queue[self.count] = data
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("[INFO] Queue is Empty!")
            return
        
        data = self.queue[0]
        for i in range(1, self.count):
            self.queue[i - 1] = self.queue[i]
        self.queue[self.count - 1] = None
        self.count -= 1
        return data

    def display_queue(self):
        print("[INFO] Queue:", self.queue)