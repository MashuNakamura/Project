# Ada 3 botol: satu racun, satu wine, satu air.
# Petunjuk: Botol 1 di sebelah air. Botol 3 bukan racun.

bottles = ["?", "?", "?"]
bottles[1] = "air"  # Misal sudah diketahui dari petunjuk lain
bottles[2] = "wine"  # Karena botol 3 bukan racun
bottles[0] = "racun"  # Sisa botol 1 adalah racun
print("Isi botol:", bottles)