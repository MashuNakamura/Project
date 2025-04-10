from mesin_mobil import MesinMobil

class Mobil:
    def __init__(self, warna, model, cc_mesin):
        self.warna = warna
        self.model = model
        self.mesin = MesinMobil(cc_mesin)

    def jalankan_mesin(self):
        return f"{self.mesin.jalankan_mesin()} Tipe mesin: {self.mesin.cc} cc. Mobil model {self.model} warna {self.warna}."

    def hentikan_mesin(self):
        return f"{self.mesin.hentikan_mesin()} Tipe mesin: {self.mesin.cc} cc. Mobil model {self.model} warna {self.warna}."