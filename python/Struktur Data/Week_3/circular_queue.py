class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Penuh!")
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue Kosong!")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed

    def display(self):
        if self.front == -1:
            print("Queue Kosong!")
            return
        i = self.front
        print("Isi Queue :", end=" ")
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

if __name__ == "__main__":
    size = int(input("Masukkan ukuran queue : "))
    cq = CircularQueue(size)

    while True:
        print("======= MENU =======")
        print("1. Enqueue (Tambah)")
        print("2. Dequeue (Hapus)")
        print("3. Tampilkan Queue")
        print("4. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            data = input("Masukkan data yang ingin ditambahkan : ")
            cq.enqueue(data)
        elif pilihan == "2":
            removed = cq.dequeue()
            print(f"Data yang dihapus: {removed}")
        elif pilihan == "3":
            cq.display()
        elif pilihan == "4":
            print("Tuhan Memberkati.")
            break
        else:
            print("Invalid Menu")