from bintang import bintang
from number import number

if __name__ == "__main__":
    while True:
        print("\n==================")
        print("0. Exit")
        print("1. bintang 1")
        print("2. bintang 2")
        print("==================")
        menu = input("Pilih Menu : ")
        
        if menu == "1":
            obj = bintang()
            obj.input_n()
            obj.cek_syarat()
            obj.cetak_bintang()

        elif menu == "2":
            obj = number()
            obj.input_n()
            obj.cek_syarat()
            obj.cetak_number()

        elif menu == "0":
            print("Terima Kasih telah menggunakan program ini")
            break

        else:
            print("Nomor Menu tidak valid")