class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = - 1

    def is_empty(self):
        return self.front == - 1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue Penuh!")
            return
        
        if self.front == - 1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Kosong!")
            return None
        
        removed = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = - 1
        else:
            self.front = (self.front + 1) % self.size
        return removed

    def display(self):
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print(f"Queue : {result}")