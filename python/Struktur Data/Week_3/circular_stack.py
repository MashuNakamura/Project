class CircularStack:
    def __init__ (self, size):
        self.size = size
        self.stack = [None] * size
        self.top = - 1
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def push(self, data):
        if self.is_full():
            print("Stack is Full")
            return
        self.top = (self.top + 1) % self.size
        self.stack[self.top] = data
        self.count += 1
        print(f"Added data : {data}")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        popped = self.stack[self.top]
        self.stack[self.top] = None
        self.top = (self.top - 1 + self.size) % self.size
        self.count -= 1
        print(f"Popped data : {popped}")
        return popped
    
    def display_stack(self):
        print(f"Stack : {self.stack}")
        
    def display_count(self):
        print(f"Count : {self.count}")

if __name__ == "__main__":
    size = int(input("Masukkan ukuran queue : "))
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
            print("Tuhan Memberkati.")
            break

        else:
            print("Invalid Menu")