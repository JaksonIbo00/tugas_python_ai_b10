print("========== List - akses & manipulasi ==========")
data_list = ["Jakson", 17.2, "AI", 10, 275, 5.5, "IL"]
print("List : ", data_list)
print("Elemen pertama : ", data_list[0])
print("Elemen terakhir : ", data_list[-1])
print("Slicing[0:5:3] : ", data_list[0:5:3])
print(" ")

print("List : ", data_list)
data_list.append(8)
print("Setelah append (8) : ", data_list)

data_list.insert(2, "new")
print("Setelah insert (new) : ", data_list)

data_list.extend(["apel", "jeruk"])
print("Setelah extend (apel,jeruk) : ", data_list)

data_list.pop()
print("Setelah pop : ", data_list)

data_list.remove("new")
print("Setelah remove (new) : ", data_list)
print(" ")

print("========== Tuple - immutability & unpacking ==========")
tuple = ("rimuru", 2026, "furab", 1, 11, "nana")
print("Tuple : ", tuple)
print("Panjang tuple : ", len(tuple))
print("Akses indeks ke-2 : ", tuple[2])
print(" ")

#Unpacking
a, b, c, *rest = tuple
print("Unpacking : ")
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("Rest = ", rest)
print(" ")

print("========== Set - keunikan & operasi himpunan ==========")
set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}
print("Set 1 : ", set1)
print("Set 2 : ", set2)
print(" ")

print("Union : ", set1 | set2)
print("Intersection : ", set1 & set2)
print("Difference 1 : ", set1 - set2)
print("Difference 2 : ", set2 - set1)
print("Symmetric Difference : ", set1 ^ set2)
print(" ")

#Duplikat hilang
set_duplikat = {1, 1, 2, 3, 3, 4, 5}
print("Set tanpa duplikat : ", set_duplikat)
print(" ")

print("========== Dictionary - key/value dasar ==========")
data_mahasiswa = {
    "nama" : "jakson",
    "nim" : "202365012",
    "angkatan" : "2023",
    "kota" : "manokwari"    
}
print(" Data mahasiswa : ", data_mahasiswa)

data_mahasiswa["jurusan"] = "teknik informatika"
data_mahasiswa["kota"] = "biak"
del data_mahasiswa["kota"]
print("Data setelah perubahan : ", data_mahasiswa)
print(" ")

print("Keys : ", data_mahasiswa.keys())
print("Values : ", data_mahasiswa.values())
print("Items : ", data_mahasiswa.items())
print(" ")

print("Iterasi : ")
for x, y in data_mahasiswa.items():
    print(x, ":", y)
print(" ")

print("========== Nested structures ==========")
buku = [
    {"judul": "Anak emas", "penulis": "jakson", "tahun": 2019},
    {"judul": "Dunia bulat", "penulis": "Robert", "tahun": 2022},
    {"judul": "Rumah kuning", "penulis": "grace", "tahun": 2025},
    {"judul": "Aku", "penulis": "dance", "tahun": 2020},
    {"judul": "Pohon toge", "penulis": "sweety", "tahun": 2023}
]

print("Daftar judul buku : ")
for b in buku:
    print("-", b["judul"])
print(" ") 

filter_buku = [b for b in buku if b["tahun"] >= 2021]
print(" Buku terbitan >= 2021 : ", filter_buku)
print(" ")


print("========== Comprehension & utilitas ==========")
angka = list(range(1, 21))

angka_genap = [x for x in angka if x % 2 == 0]
angka_kuadrat = [x**2 for x in angka]
print("Angka genap : ", angka_genap)
print("Angka kuadrat : ", angka_kuadrat)
print(" ")

mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range (1, 11)}
print("Mapping angka : ", mapping)
print(" ")

kalimat = "nama saya budi"
huruf_unik = {a.lower() for a in kalimat if a.isalpha()}
print("Huruf unik : ", huruf_unik)
print(" ")

print("========== Keanggotaan & pencarian sederhana ==========")
buah = ["mangga", "anggur", "markisa", "duku"]
print("Apakah 'duku' ada?", "duku" in buah)
print("Apakah 'apel' ada?", "apel" in buah)

if "anggur" in buah:
    print("Posisi buah anggur : ", buah.index("anggur"))
print(" ")
    
number = {1, 2, 3, 4, 5}
print("Apakah 3 ada di list number?", 3 in number)
print("Apakah 7 ada di list number?", 7 in number)
print(" ")