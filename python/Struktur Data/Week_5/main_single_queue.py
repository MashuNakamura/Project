from single_queue import Queue

if __name__ == "__main__":
    size = int(input("Masukkan ukuran stack : "))
    q = Queue(size)
    while True:
        print("======= MENU =======")
        print("1. Enqueue (Add)")
        print("2. Dequeue (Delete)")
        print("3. Tampilkan Queue")
        print("4. Tampilkan Count")
        print("5. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            data = int(input("Masukkan data : "))
            q.enqueue(data)

        elif pilihan == "2":
            q.dequeue()
            
        elif pilihan == "3":
            q.display_queue()

        elif pilihan == "4":
            q.display_count()

        elif pilihan == "5":
            print("Tuhan Memberkati.")
            break

        else:
            print("Invalid Menu")
            continue