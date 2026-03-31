# IMPORT & SETUP

import numpy as np
import pandas as pd
import os

np.random.seed(42)

# NUMPY – DATA & STATISTIK
nilai_ujian = np.random.randint(50, 100, size=12)

rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

# PANDAS – DATAFRAME
data = {
    "nama": ["jakson", "robert", "sweety", "miqdad", "novi"],
    "nim": ["202365001", "202365010", "202365040", "202365006", "202365016"],
    "nilai": nilai_ujian[:5]
}

df = pd.DataFrame(data)

df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# FILE I/O – RINGKASAN
file_path = "ringkasan_tugas6.txt"

def tulis_ringkasan_awal():
    with open(file_path, "w") as f:
        f.write("=========== RINGKASAN STATISTIK NUMPY ==========\n")
        f.write(f"Rata-rata : {rata:.2f}\n")
        f.write(f"Median    : {median:.2f}\n")
        f.write(f"Std Dev   : {std_dev:.2f}\n")
        f.write(f"Min       : {nilai_min}\n")
        f.write(f"Max       : {nilai_max}\n\n")

        f.write("========== RINGKASAN DATAFRAME ==========\n")
        f.write(f"Jumlah data      : {len(df)}\n")
        f.write(f"Jumlah LULUS     : {len(df[df['status']=='LULUS'])}\n")
        f.write(f"Jumlah TIDAK LULUS : {len(df[df['status']=='TIDAK LULUS'])}\n\n")


# OOP – CLASS GRADEBOOK
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = len(self.df[self.df["nilai"] >= threshold])
        return (lulus / total) * 100 if total > 0 else 0.0

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("========== RINGKASAN DARI CLASS GRADEBOOK ==========\n")
            f.write(f"Jumlah data : {len(self.df)}\n")
            f.write(f"Rata-rata   : {self.average():.2f}\n")
            f.write(f"Pass rate   : {self.pass_rate():.2f}%\n\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average():.2f})"


# DEMO
if __name__ == "__main__":
    print("========== NUMPY ==========")
    print("Data nilai:", nilai_ujian)
    print(f"Rata-rata : {rata:.2f}")
    print(f"Median    : {median:.2f}")
    print(f"Std Dev   : {std_dev:.2f}")
    print(f"Min       : {nilai_min}")
    print(f"Max       : {nilai_max}")

    print("========== PANDAS ==========")
    print(df.head())

    print("========== OOP: GRADEBOOK ==========")
    gb = GradeBook(df)
    print(gb)
    print(f"Average   : {gb.average():.2f}")
    print(f"Pass Rate : {gb.pass_rate():.2f}%")

    # Tulis file ringkasan
    tulis_ringkasan_awal()
    gb.save_summary(file_path)

    print(f"Ringkasan telah disimpan ke file: {file_path}")