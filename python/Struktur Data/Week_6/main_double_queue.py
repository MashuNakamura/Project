from double_queue import Queue

if __name__ == "__main__":
    size = int(input("Masukkan ukuran queue: "))
    q = Queue(size)

    while True:
        print("\n======= MENU =======")
        print("1. Enqueue Front")
        print("2. Dequeue Front")
        print("3. Enqueue Back")
        print("4. Dequeue Back")
        print("5. Tampilkan Queue")
        print("6. Tampilkan Count")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            data = int(input("Masukkan data untuk Enqueue Front: "))
            q.enqueue_front(data)

        elif pilihan == "2":
            removed_data = q.dequeue_front()
            if removed_data is not None:
                print(f"Data yang dihapus dari depan: {removed_data}")
            else:
                print("Tidak ada data yang bisa dihapus, queue kosong!")

        elif pilihan == "3":
            data = int(input("Masukkan data untuk Enqueue Back: "))
            q.enqueue_back(data)

        elif pilihan == "4":
            removed_data = q.dequeue_back()
            if removed_data is not None:
                print(f"Data yang dihapus dari belakang: {removed_data}")
            else:
                print("Tidak ada data yang bisa dihapus, queue kosong!")

        elif pilihan == "5":
            q.display_queue()

        elif pilihan == "6":
            q.display_count()

        elif pilihan == "7":
            print("Terima kasih, Tuhan Yesus Memberkati.")
            break

        else:
            print("Menu tidak valid. Silakan pilih menu yang benar.")