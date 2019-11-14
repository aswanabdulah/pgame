# Buat variabel dan memberikan elemen
buah=["Durian","Mangga","Rambutan"]

# cetak list buah
print(buah)

print("Sebelum ditambah :", buah)
# tambah elemen ke dalam list buah di bagian akhir
buah.append("Anggur")
print("Setelah ditambah :", buah)

# tambah elemen ke list sesuai posisi (0 adalah diawal)
buah.insert(0, "Pepaya")
print("Setelah ditambah :", buah)

# hapus elemen list yang ke 1 (1 adalah bagian ke 2)
buah.remove(buah[1])
print("Setelah dihapus [1] :", buah)

# hapus elemen list yang bernilai "Anggur"
buah.remove("Anggur")
print("Setelah dihapus (Anggur) : ", buah)
