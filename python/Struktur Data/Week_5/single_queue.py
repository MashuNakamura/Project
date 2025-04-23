class Queue:
    def __init__ (self, size):
        self.size = size
        self.queue = [None] * size
        self.tail = size - 1 
        self.head = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def display_queue(self):
        print(f"Queue : {self.queue}")

    def display_count(self):
        print(f"Count : {self.count}")

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full !")
            return
        
        self.tail = (self.tail + 1) % self.size 
        self.queue[self.tail] = data
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty !")
            return

        data = self.queue[0]
        for i in range(1, self.count):
            self.queue[i - 1] = self.queue[i]
            
        self.tail = (self.tail - 1) % self.size 
        self.queue[self.count - 1] = None
        self.count -= 1
        return data