# Deklarasi Variabel dan Tipe Data
nama = "Jakson"                                           #String
umur = 21                                                 #Integer
tinggi = 169.5                                            #Float
mahasiswa = True                                          #Boolean
hobi = ["Mendengar musik", "Bermain game", "Membaca"]     #List
print(" ")

print("========== Manipulasi string ==========")
print(" ")
print("Nama :", nama)
print("Umur :", umur)
print("Tinggi :", tinggi)
print("Apakah anda seorang mahasiswa?", mahasiswa)
print("hobi :", hobi)
print(" ")

print("Panjang teks:", len(nama))
print("Huruf besar:", nama.upper())
print("Huruf kecil:", nama.lower())
print(" ")

print("========== Operasi Matematika Sederhana ==========")
x = 2
y = 5
z = 8

Penjumlahan = x + y
Pengurangan = z - y
Perkalian = x * z
Pembagian = z / y
Pembagian_bil_bulat = z // x
Sisa_bagi = y % x

print(" ")
print(Penjumlahan)
print(Pengurangan)
print(Perkalian)
print(Pembagian)
print(Pembagian_bil_bulat)
print(Sisa_bagi)
print(" ")

print("========== List dan Akses Elemen ==========")
print(" ")
print("List hobi:", hobi)
print("Elemen pertama :", hobi[0])
print("Elemen terakhir :", hobi[2])
hobi.append("Menggambar")
print("Hobi setelah ditambah :", hobi)
hobi.remove("Bermain game")
print("Hobi setelah dikurangi :", hobi)
print(" ")

print("========== Input User ==========")
nama_user = input("Masukkan nama anda : ")
umur_user = input("Masukkan usia anda : ")
pekerjaan = input("Masukkan pekerjaan anda : ")
print("Halo, nama saya", nama_user + ",", "umur saya", umur_user, "tahun, ", "pekerjaan saya adalah", pekerjaan)



