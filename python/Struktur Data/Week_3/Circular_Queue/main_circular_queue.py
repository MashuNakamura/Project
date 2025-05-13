from circular_queue import CircularQueue

if __name__ == "__main__":
    size = int(input("Input queue size : "))
    cq = CircularQueue(size)

    while True:
        print("======= MENU =======")
        print("1. Enqueue (Add)")
        print("2. Dequeue (Delete)")
        print("3. Show Queue")
        print("4. Exit")
        print("====================")
        pilihan = input("Select menu : ")

        if pilihan == "1":
            data = input("[INFO] Input new data : ")
            cq.enqueue(data)

        elif pilihan == "2":
            removed = cq.dequeue()
            if removed is not None:
                print(f"[INFO] Deleted data: {removed}")

        elif pilihan == "3":
            cq.display()

        elif pilihan == "4":
            print("[INFO] God Bless You.")
            break
        
        else:
            print("[INFO] Invalid Menu")