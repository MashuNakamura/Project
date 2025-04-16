from pelajar import pelajar

class mahasiswa(pelajar):
    def status(self):
        self.nama = input("Nama : ")
        self.alamat = input("Alamat : ")
        self.jenis_kelamin = input("Jenis Kelamin : ")
        self.tingkat = input("NRP : ")
        return f"Nama : {self.nama}, alamat : {self.alamat}, jenis kelamin : {self.jenis_kelamin}, NRP : {self.tingkat}"