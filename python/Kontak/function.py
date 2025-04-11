def take_name(daftar_kontak):
    for i, kontak in enumerate(daftar_kontak, start=1):
        print(f"{i}. {kontak['nama']}")
    print("0. Kembali")
    print("===========================")

def display_kontak(daftar_kontak, index: int):
    if 0 <= index < len(daftar_kontak):
        selected = daftar_kontak[index]
        print("===========================")
        print(f"Nama    : {selected["nama"]}")
        print(f"Email   : {selected["email"]}")
        print(f"Telepon : {selected["telepon"]}")
        print("===========================")
    else:
        print("===========================")
        print("Tidak ada dalam List !")
        print("===========================")

def kontak_baru():
    nama = input("Masukkan Nama : ")
    email = input("Masukkan Email : ")
    telepon = input("Masukkan No Telp : ")
    tmp_kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    print(f"{nama} berhasil ditambahkan")
    return tmp_kontak

def hapus_kontak(daftar_kontak):
    for i, value in enumerate(daftar_kontak, start = 1):
        print(f"{i}. {value["nama"]}")

    user = int(input("Nomor Berapa yang ingin dihapus? "))

    if 1 <= user <= len(daftar_kontak):
        deleted = daftar_kontak.pop(user - 1)
        print(f"{deleted["nama"]} berhasil dihapus.")
    else:
        print("Nomor tidak valid.")

def cari_kontak(daftar_kontak):
    while True:
        print("===========================")
        print("1. Nama")
        print("2. Number")
        print("0. Kembali")
        print("===========================")
        check = int(input("Search mode : "))
        check_boolean = False
        
        if check == 1:
            search = input("Cari kontak dengan nama : ").lower()
            for kontak in daftar_kontak:
                if search in kontak['nama'].lower():
                    print("===========================")
                    print(f"Nama    : {kontak['nama']}")
                    print(f"Email   : {kontak['email']}")
                    print(f"Telepon : {kontak['telepon']}")
                    check_boolean = True
            if check_boolean == False:
                print("===========================")
                print("Tidak ditemukan")
                print("===========================")
            continue

        elif check == 2:
            search = input("Cari kontak dengan nomor : ")
            for kontak in daftar_kontak:
                if search in kontak["telepon"]:
                    print("===========================")
                    print(f"Nama    : {kontak['nama']}")
                    print(f"Email   : {kontak['email']}")
                    print(f"Telepon : {kontak['telepon']}")
                    check_boolean = True
            if check_boolean == False:
                print("===========================")
                print("Tidak ditemukan")
                print("===========================")
            continue
        elif check == 0:
            break
        else:
            print("Pilihan tidak valid. Masukkan 1 atau 2.")
            continue