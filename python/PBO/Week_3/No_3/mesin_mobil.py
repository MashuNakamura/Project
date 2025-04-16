class MesinMobil:
    def __init__(self, cc):
        self.cc = cc

    def tampilkan_cc(self):
        return f"Mesin ini memiliki kapasitas {self.cc} cc."

    def jalankan_mesin(self):
        return "Mesin mobil dijalankan."

    def hentikan_mesin(self):
        return "Mesin mobil dihentikan."