import function

daftar_kontak = [
    { "nama": "Mashu", "email": "federicomatthewpratamaa@gmail.com", "telepon": "00000" },
    { "nama": "Arthur", "email": "arthur@gmail.com", "telepon": "2221112" },
    { "nama": "Badut", "email": "anjingkaubadutbeban@gmail.com", "telepon": "12121131" },
    { "nama": "Jefferey", "email": "jeffereymonyet@gmail.com", "telepon": "12345" }
]

while True:
    print("===========================")
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("TODO : Can Edit Contact ?")
    print("0. Keluar")
    print("===========================")

    menu = input("Pilih menu : ")
    if menu == "0":
        break

    elif menu == "1":
        while True:
            function.take_name(daftar_kontak)
            menu_kontak = int(input("Pilih Nama Kontak : "))
            if menu_kontak == 0:
                break
            function.display_kontak(daftar_kontak, int(menu_kontak) - 1)

    elif menu == "2":
        kontak = function.kontak_baru()
        daftar_kontak.append(kontak)

    elif menu == "3":
        kontak = function.hapus_kontak(daftar_kontak)

    elif menu == "4":
        kontak = function.cari_kontak(daftar_kontak)

    else:
        print("Data Harus Integer !")

print("Tuhan Memberkati.")
