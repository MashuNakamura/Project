class double_stack():
    # Declare Data
    def __init__(self, size):
        self.size = size 
        self.dataset = [None] * size
        self.top1 = - 1
        self.top2 = size

    # Function Push data to Top1
    def push1(self, data):
        if self.top2 - self.top1 > 1:
            self.top1 += 1
            self.dataset[self.top1] = data
        else:
            print("Stack 1 Penuh")

    # Function Push data to Top2
    def push2(self, data):
        if self.top2 - self.top1 > 1:
            self.top2 -= 1
            self.dataset[self.top2] = data
        else:
            print("Stack 2 Penuh")

    # Function Pop Data Top1
    def pop1(self):
        if self.top1 == - 1:
            print("Stack 1 Kosong")
        else:
            print(f"Data {self.dataset[self.top1]} berhasil di pop dari Stack 1")
            self.top1 -= 1

    # Function Pop Data Top2
    def pop2(self):
        if self.top2 == self.size:
            print("Stack 2 Kosong")
            return
        else:
            print(f"Data {self.dataset[self.top2]} berhasil di pop dari Stack 2")
            self.top2 += 1

    # Function Peek Data Top1
    def peek1(self):
        if self.top1 == - 1:
            print("Stack 1 Kosong")
        else:
            print(f"Mengintip Stack 1 : {self.dataset[self.top1]}")

    # Function Peek Data Top2
    def peek2(self):
        if self.top2 == self.size:
            print("Stack 1 Kosong")
        else:
            print(f"Mengintip Stack 2 : {self.dataset[self.top2]}")

    # Function Clear Data Top1
    def clear1(self):
        print("Stack 1 Berhasil di Clear")
        for i in range (0, self.top1):
            self.dataset[i] = None
            self.top1 = -1

    # Function Clear Data Top2
    def clear2(self):
        print("Stack 2 Berhasil di Clear")
        for i in range (0, self.top2):
            self.dataset[i] = None
            self.top2 = self.size

    # Function Print Top1
    def print_stack1(self):
        if self.top1 == - 1:
            print("Data Kosong")
        else:
            print(f"{self.dataset[0:self.top1 + 1]}")

    # Function Print Top2
    def print_stack2(self):
        if self.top2 == self.size:
            print("Data Kosong")
        else:
            print(f"{self.dataset[self.top2:self.size]}")

if __name__ == "__main__":
    # Input Size
    user_dataset = int(input("Masukkan Size Dataset : "))
    ds = double_stack(user_dataset)

    # Looping Menu
    while True:
        print("=======================")
        print("1. Push Stack 1")
        print("2. Push Stack 2")
        print("3. Pop Stack 1")
        print("4. Pop Stack 2")
        print("5. Lihat Isi Stack 1")
        print("6. Lihat Isi Stack 2")
        print("7. Peek Data Stack 1")
        print("8. Peek Data Stack 2")
        print("9. Delete Pop Stack 1")
        print("10. Delete Pop Stack 2")
        print("0. Keluar")
        print("=======================")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            data = input("Masukkan data untuk Stack 1: ")
            ds.push1(data)

        elif pilihan == "2":
            data = input("Masukkan data untuk Stack 2: ")
            ds.push2(data)

        elif pilihan == "3":
            ds.pop1()
            
        elif pilihan == "4":
            ds.pop2()

        elif pilihan == "5":
            ds.print_stack1()

        elif pilihan == "6":
            ds.print_stack2()

        elif pilihan == "7":
            ds.peek1()

        elif pilihan == "8":
            ds.peek2()

        elif pilihan == "9":
            ds.clear1()

        elif pilihan == "10":
            ds.clear2()

        elif pilihan == "0":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")