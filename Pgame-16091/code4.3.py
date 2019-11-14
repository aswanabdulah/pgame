# Buat variabel dan memberikan nilai
prodi = "Teknik Informatika"
konsen = "Jaringan"
mata_kuliah = "Pemrograman Game"
kampus = "UMMU"
lokasi = "Ternate"
tahun = 2019

# Menampilkan nilai variabel ke layar
print(prodi)
print(konsen)
print(mata_kuliah)
print(kampus)
print(lokasi)

# Cetak '-' sebanyak 35 kali
print( '*' * 35 )

# Cetak nilai variabel ke layar dengan keterangan
print("Prodi : ", prodi)
print("Konsentrasi : ", konsen)
print("Mata Kuliah : ", mata_kuliah)
print("Kampus : %s " % kampus)
print("Lokasi : %s " % lokasi)
print("Tahun : %d " % tahun)

# Cetak '-' sebanyak 35 kali
print( '*' * 35 )

# Cetak variabel prodi dan kampus
print("Prodi & Kampus : ", prodi, ",", kampus) # cara 1
print("Prodi dan Kampus : ", prodi + ", " + kampus) # cara 2
print("Prodi dan Kampus : %s, %s " % (prodi, kampus))# cara 3
