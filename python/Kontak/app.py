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
    print("1. Daftar Kontak (Asc)")
    print("2. Daftar Kontak (Desc)")
    print("3. Detail Kontak")
    print("4. Tambah Kontak")
    print("5. Edit Kontak")
    print("6. Hapus Kontak")
    print("7. Cari Kontak")
    print("0. Keluar")
    print("===========================")

    menu = input("Pilih menu : ")
    if menu == "0":
        break

    elif menu == "1":
        function.take_name_asc(daftar_kontak)
        
    elif menu == "2":
        function.take_name_desc(daftar_kontak)

    elif menu == "3":
        while True:
            function.detail_name(daftar_kontak)
            menu_kontak = int(input("Pilih Nama Kontak : "))
            if menu_kontak == 0:
                break
            function.display_kontak(daftar_kontak, int(menu_kontak) - 1)

    elif menu == "4":
        kontak = function.kontak_baru()
        daftar_kontak.append(kontak)
        
    elif menu == "5":
        kontak = function.edit_kontak(daftar_kontak)

    elif menu == "6":
        kontak = function.hapus_kontak(daftar_kontak)

    elif menu == "7":
        kontak = function.cari_kontak(daftar_kontak)
    
    else:
        print("Data Harus Integer !")

print("Tuhan Memberkati.")