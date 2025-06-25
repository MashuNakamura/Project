class Jalur:
    def __init__(self, nama):
        self.nama = nama
        self.langkah = []
    
    def input_jalur(self):
        banyak_langkah = int(input(f"Masukkan jumlah langkah untuk {self.nama}: "))
        print(f"Masukkan data (dari ke bobot), contoh: 1 2 4")
        for i in range(banyak_langkah):
            data = input(f"Langkah ke-{i+1}: ").split()
            dari, ke, bobot = map(int, data)
            self.langkah.append((dari, ke, bobot))
    
    def hitung_bobot(self):
        return sum(bobot for _, _, bobot in self.langkah)
    
    def tampilkan(self):
        if not self.langkah:
            return "-"
        rute = ' -> '.join(str(dari) for dari, _, _ in self.langkah) + f" -> {self.langkah[-1][1]}"
        return rute

jalur1 = Jalur("Jalur 1")
jalur2 = Jalur("Jalur 2")

jalur1.input_jalur()
jalur2.input_jalur()

bobot1 = jalur1.hitung_bobot()
bobot2 = jalur2.hitung_bobot()

if bobot1 > bobot2:
    jalur_terbesar, bobot_terbesar = jalur1, bobot1
    jalur_terkecil, bobot_terkecil = jalur2, bobot2
else:
    jalur_terbesar, bobot_terbesar = jalur2, bobot2
    jalur_terkecil, bobot_terkecil = jalur1, bobot1

print("\nJalur dengan bobot terbesar:", jalur_terbesar.nama)
print("  Rute :", jalur_terbesar.tampilkan())
print("  Bobot:", bobot_terbesar)
print("\nJalur dengan bobot terkecil:", jalur_terkecil.nama)
print("  Rute :", jalur_terkecil.tampilkan())
print("  Bobot:", bobot_terkecil)