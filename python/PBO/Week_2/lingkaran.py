from shape import Shape

class lingkaran:
    def user_input(self):
        self.r = int(input("masukkan nilai jari-jari : "))
        
    def hasil_luas(self):
        return 3.14 * (self.r ** 2)