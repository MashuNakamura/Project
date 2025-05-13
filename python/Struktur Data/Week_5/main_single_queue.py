from single_queue import Queue

if __name__ == "__main__":
    size = int(input("Masukkan ukuran stack : "))
    q = Queue(size)
    while True:
        print("======= MENU =======")
        print("1. Enqueue (Add)")
        print("2. Dequeue (Delete)")
        print("3. Show Queue")
        print("4. Show Count")
        print("5. Exit")
        print("====================")

        menu = input("Select menu : ")

        if menu == "1":
            data = int(input("[INFO] Input new data : "))
            q.enqueue(data)

        elif menu == "2":
            q.dequeue()
            
        elif menu == "3":
            q.display_queue()

        elif menu == "4":
            q.display_count()

        elif menu == "5":
            print("[INFO] God Bless You.")
            break

        else:
            print("[INFO] Invalid Menu")
            continue