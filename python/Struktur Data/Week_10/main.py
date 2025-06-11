from mahasiswa import Mahasiswa

if __name__ == "__main__":
    mhs1 = Mahasiswa("Budi", "Jl. Merdeka No. 1")

    mhs1.tambah(Mahasiswa("Andi", "Jl. Merdeka No. 2"))
    mhs1.tambah(Mahasiswa("Citra", "Jl. Pancasila No. 3"))

    mhs1.tampilkan()