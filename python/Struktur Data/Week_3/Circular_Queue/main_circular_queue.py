from circular_queue import CircularQueue

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
            if removed is not None:
                print(f"Data yang dihapus: {removed}")

        elif pilihan == "3":
            cq.display()

        elif pilihan == "4":
            print("Tuhan Memberkati.")
            break
        
        else:
            print("Invalid Menu")