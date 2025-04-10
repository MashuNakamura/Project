from transportasi import alat_transportasi

class sepeda_motor(alat_transportasi):
    def bergerak(self, nama_kendaraan : str = "Motor Umum"):
        nama_kendaraan = input("Nama Motor : ")
        return f"Transportasi Motor {nama_kendaraan} bergerak"