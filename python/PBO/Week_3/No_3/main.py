from mobil import Mobil

if __name__ == "__main__":
    print("=== Input Data Mobil ===")
    warna = input("Masukkan warna mobil : ")
    model = input("Masukkan model mobil : ")
    cc = input("Masukkan kapasitas cc mesin : ")

    mobil = Mobil(warna, model, cc)

    print("\n" + mobil.jalankan_mesin())
    print(mobil.hentikan_mesin())