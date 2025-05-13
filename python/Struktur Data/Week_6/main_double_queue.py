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
        print("5. Show Queue")
        print("6. Show Count")
        print("7. Exit")

        pilihan = input("[INFO] Select menu: ")

        if pilihan == "1":
            data = int(input("[INFO] Input new Front data : "))
            q.enqueue_front(data)

        elif pilihan == "2":
            removed_data = q.dequeue_front()
            if removed_data is not None:
                print(f"[INFO] Deleted Front data : {removed_data}")

        elif pilihan == "3":
            data = int(input("[INFO] Input new Back data : "))
            q.enqueue_back(data)

        elif pilihan == "4":
            removed_data = q.dequeue_back()
            if removed_data is not None:
                print(f"[INFO] Deleted Back data : {removed_data}")

        elif pilihan == "5":
            q.display_queue()

        elif pilihan == "6":
            q.display_count()

        elif pilihan == "7":
            print("[INFO] God Bless You.")
            break

        else:
            print("[INFO] Invalid Menu.")