from mobil import mobil
from sepeda_motor import sepeda_motor

if __name__ == "__main__":
    while True:
        print("==================")
        print("0. Exit")
        print("1. Sepeda Motor")
        print("2. Mobil")
        print("==================")
        menu = input("Pilih Menu : ")
        
        if menu == "1":
            print(sepeda_motor().bergerak())

        elif menu == "2":
            print(mobil().bergerak())

        elif menu == "0":
            print("Terima Kasih telah menggunakan program ini")
            break

        else:
            print("Nomor Menu tidak valid")