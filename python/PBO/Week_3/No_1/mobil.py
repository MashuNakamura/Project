from transportasi import alat_transportasi

class mobil(alat_transportasi):
    def bergerak(self, nama_kendaraan : str = "Mobil Umum"):
        nama_kendaraan = input("Nama Mobil : ")
        return f"Transportasi Mobil {nama_kendaraan} bergerak"