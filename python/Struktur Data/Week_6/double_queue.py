class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.tail = size - 1
        self.head = 0
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def display_queue(self):
        print(f"[INFO] Queue : {self.queue}")

    def display_count(self):
        print(f"[INFO] Count : {self.count}")

    def enqueue_front(self, data):
        if self.is_full():
            print("[INFO] Queue is Full!")
            return

        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = data
        self.count += 1

    def dequeue_front(self):
        if self.is_empty():
            print("[INFO] Queue is Empty!")
            return

        data = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail - 1 + self.size) % self.size
        self.count -= 1
        return data

    def enqueue_back(self, data):
        if self.is_full():
            print("[INFO] Queue is Full!")
            return

        self.head = (self.head - 1 + self.size) % self.size
        self.queue[self.head] = data
        self.count += 1

    def dequeue_back(self):
        if self.is_empty():
            print("[INFO] Queue is Empty!")
            return

        data = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return data