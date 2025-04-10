from pelajar import pelajar

class siswa(pelajar):
    def status(self):
        self.nama = input("Nama : ")
        self.alamat = input("Alamat : ")
        self.jenis_kelamin = input("Jenis Kelamin : ")
        self.tingkat = input("NISN : ")
        return f"Nama : {self.nama}, alamat : {self.alamat}, jenis kelamin : {self.jenis_kelamin}, NISN : {self.tingkat}"