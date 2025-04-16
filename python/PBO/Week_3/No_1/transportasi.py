class alat_transportasi():
    def __init__ (self, nama_kendaraan : str = "Umum"):
        self.nama_kendaraan = nama_kendaraan
    
    def bergerak(self) -> None:
        return f"Transportasi {self.nama_kendaraan} bergerak"