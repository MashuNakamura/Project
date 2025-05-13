from circular_stack import CircularStack

if __name__ == "__main__":
    size = int(input("Masukkan ukuran stack : "))
    cs = CircularStack(size)

    while True:
        print("======= MENU =======")
        print("1. Push (Add)")
        print("2. Pop (Delete)")
        print("3. Tampilkan Stack")
        print("4. Tampilkan Count")
        print("5. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            data = int(input("Masukkan data : "))
            cs.push(data)

        elif pilihan == "2":
            cs.pop()
            
        elif pilihan == "3":
            cs.display_stack()

        elif pilihan == "4":
            cs.display_count()

        elif pilihan == "5":
            print("[INFO] Tuhan Memberkati.")
            break

        else:
            print("[INFO] Invalid Menu")
            continue