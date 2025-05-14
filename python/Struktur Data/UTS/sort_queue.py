class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size
    
    def display_queue(self):
        print("[INFO] Queue:", self.queue)
        
    def display_count(self):
        print("[INFO] Queue:", self.count)

    def enqueue(self, data):
        if self.is_full():
            print("[INFO] Queue is Full!")
            return
        
        pos = 0
        
        while pos < self.count and self.queue[pos] < data:
            pos += 1
        
        for i in range(self.count, pos, -1):
            self.queue[i] = self.queue[i - 1]
        
        self.queue[pos] = data
        self.count += 1
        print(f"[INFO] Data {data} has been added")
            
    def dequeue(self):
        if self.is_empty():
            print("[INFO] Queue is Empty!")
            return
        
        data = self.queue[0]
        for i in range(1, self.count):
            self.queue[i - 1] = self.queue[i]
        self.queue[self.count - 1] = None
        self.count -= 1
        print(f"[INFO] Data {data} has been deleted")
        return data