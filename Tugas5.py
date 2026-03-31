def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)
print(" ")

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self):
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"
print(" ")

if __name__ == "__main__":
    print("============ FUNCTIONS ============")
    print(" ")
    print(greet("Arifian"))

    print("Tambah 5 + 7 =", tambah(5, 7))
    print("Tambah 10 =", tambah(10))

    print("Rata-rata [80, 90, 100] =", rata_rata([80, 90, 100]))
    print("Rata-rata [] =", rata_rata([]))
    print(" ")
    
    print("========== CLASS STUDENT ==========")
    print(" ")
    mahasiswa1 = Student("Jakson", "202365012")
    mahasiswa1.tambah_nilai(95)
    mahasiswa1.tambah_nilai(90)
    mahasiswa1.tambah_nilai(95)

    mahasiswa2 = Student("Andre", "202365200")
    mahasiswa2.tambah_nilai(70)
    mahasiswa2.tambah_nilai(75)
    mahasiswa2.tambah_nilai(75)
    
    print(mahasiswa1)
    print(mahasiswa2)
    print(" ")
    
    print(f"{mahasiswa1.nama} -> Rata-rata: {mahasiswa1.rata_nilai()}, Status: {mahasiswa1.status()}")
    print(f"{mahasiswa2.nama} -> Rata-rata: {mahasiswa2.rata_nilai()}, Status: {mahasiswa2.status()}")
    print(" ")