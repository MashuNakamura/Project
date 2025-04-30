import random

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = - 1
        self.random_pos = random.randint(0, self.size - 1)
        self.current_pos = self.random_pos
        self.is_first = False

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue Penuh!")
            return
        
        elif self.is_empty() and self.is_first == False:
            self.front = self.rear = self.random_pos
            self.is_first = True
        elif self.is_empty() and self.is_first == True:
            self.front = self.rear = self.current_pos
        else:
            self.rear = (self.rear + 1) % self.size
        
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Kosong!")
            return None

        removed = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = - 1
        else:
            self.front = (self.front + 1) % self.size

        return removed

    def display(self):
        visual = []

        for item in self.queue:
            if item is None:
                visual.append("None")
            else:
                visual.append(str(item))

        result = ", ".join(visual)
        print("Queue  :", f"[{result}]")