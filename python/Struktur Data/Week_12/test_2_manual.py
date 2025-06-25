jalur1 = [(1, 2, 4), (2, 4, 10)]
jalur2 = [(1, 3, 2), (3, 5, 3), (5, 4, 4)]

def hitung_bobot(jalur):
    return sum(bobot for _, _, bobot in jalur)

bobot1 = hitung_bobot(jalur1)
bobot2 = hitung_bobot(jalur2)

if bobot1 > bobot2:
    jalur_terbesar = jalur1
    bobot_terbesar = bobot1
    nama_jalur_terbesar = "Jalur 1"
    jalur_terkecil = jalur2
    bobot_terkecil = bobot2
    nama_jalur_terkecil = "Jalur 2"
else:
    jalur_terbesar = jalur2
    bobot_terbesar = bobot2
    nama_jalur_terbesar = "Jalur 2"
    jalur_terkecil = jalur1
    bobot_terkecil = bobot1
    nama_jalur_terkecil = "Jalur 1"

def tampilkan_jalur(jalur):
    return ' -> '.join(str(dari) for dari, _, _ in jalur) + f" -> {jalur[-1][1]}"

print("Jalur dengan bobot terbesar:", nama_jalur_terbesar)
print("  Rute :", tampilkan_jalur(jalur_terbesar))
print("  Bobot:", bobot_terbesar)
print()
print("Jalur dengan bobot terkecil:", nama_jalur_terkecil)
print("  Rute :", tampilkan_jalur(jalur_terkecil))
print("  Bobot:", bobot_terkecil)