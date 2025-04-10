from bilangan_n import bilangan

class number(bilangan):
    def input_n(self):
        self.n = int(input("Masukkan nilai n : "))

    def cek_syarat(self):
        return self.n >= 5 and self.n <= 89 and self.n % 2 == 1

    def cetak_number(self):
        n = self.n
        bil = 0
        for y in range(0, n - 1):
            for _ in range(y, n - 1):
                print(" ", end="")

            print(bil % 10, end="")
            bil += 1

            if y > 0:
                for _ in range(0, y * 2 - 1):
                    print(" ", end="")
                print(bil % 10, end="")
                bil += 1

            print()

        for _ in range((2 * n) - 1):
            print(bil % 10, end="")
            bil += 1
        print()