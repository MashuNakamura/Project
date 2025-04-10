from mahasiswa import mahasiswa
from siswa import siswa

if __name__ == "__main__":
    while True:
        print("==================")
        print("0. Exit")
        print("1. Mahasiswa")
        print("2. Siswa")
        print("==================")
        menu = input("Pilih Menu : ")
        
        if menu == "1":
            print(mahasiswa().status())

        elif menu == "2":
            print(siswa().status())

        elif menu == "0":
            print("Terima Kasih telah menggunakan program ini")
            break

        else:
            print("Nomor Menu tidak valid")