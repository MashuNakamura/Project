class CircularQueue:
    def __init__(self, size):
        # Deklarasi variable size (ukuran queue)
        # queue (list untuk menyimpan antrian sebanyak size), 
        # dan variable front dan rear di set ke -1 untuk menandakan kosong
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        # Kalau Rear berdekatan / mau menabrak setelah berputar, maka Queue tersebut telah Penuh
        if (self.rear + 1) % self.size == self.front:
            print("Queue Penuh!")
            return
        # Kalau front masih kosong, maka front dan rear dimulai dari index[0]
        if self.front == -1:
            self.front = self.rear = 0
        # Selain itu akan dilakukan penggeseran, contoh size : 5, apabila rear sudah menyentuh ke 5 maka ulang ke index 0
        else:
            self.rear = (self.rear + 1) % self.size

        # Untuk menyimpan queue ke data
        self.queue[self.rear] = data

    def dequeue(self):
        # Cek apabila front masih di -1, maka queue kosong
        if self.front == -1:
            print("Queue Kosong!")
            return

        # simpan nilai front
        removed = self.queue[self.front]

        # cek kalau front dan rear telah di index yang sama, maka reset
        if self.front == self.rear:
            self.front = self.rear = -1
        # kalau tidak, maka akan melakukan pergeseran index
        else:
            self.front = (self.front + 1) % self.size
        
        # nilai kembali ke removed untuk mendapatkan nilai pergeseran front
        return removed

    def display(self):
        # Cek lagi kalau front -1 maka queue kosong
        if self.front == -1:
            print("Queue Kosong!")
            return
    
        # ambil nilai front ke dalam variable i
        i = self.front
        print("Isi Queue:", end=" ")
        # looping
        while True:
            print(self.queue[i], end=" ")
            # Kalau nilai rear telah terisi, maka stop loop
            if i == self.rear:
                break
            # Front geser
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