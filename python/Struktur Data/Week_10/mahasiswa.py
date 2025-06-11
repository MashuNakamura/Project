class Mahasiswa:
    def __init__(self, nama: str, alamat: str):
        self.nama = nama
        self.alamat = alamat
        self.selanjutnya = None 

    def tambah(self, mahasiswa_baru):
        current = self
        while current.selanjutnya is not None:
            current = current.selanjutnya
        current.selanjutnya = mahasiswa_baru

    def tampilkan(self):
        current = self
        while current is not None:
            print(f"Nama   : {current.nama}")
            print(f"Alamat : {current.alamat}")
            print("----------------------")
            current = current.selanjutnya