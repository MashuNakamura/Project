from bilangan_n import bilangan

class bintang(bilangan):
    def input_n(self):
        self.n = int(input("Masukkan nilai n : "))

    def cek_syarat(self):
        return self.n >= 5 and self.n <= 89 and self.n % 2 == 1

    def cetak_bintang(self):
        n = self.n
        for y in range(0, n * 2 - 3):
            print("*", end="")
        print()
        for y in range(0, n - 2):
            print(" " * (n - y - 2), end="")
            print("*", end="")
            print(" " * (y * 2 - 1), end="")
            if(0 != y):
                print("*", end="")
            print()
        for y in range(0, n * 2 - 3):
            print("*", end="")