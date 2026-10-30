from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik, hitung_ketuntasan
from utilitas import validasi_nilai


def main():
    path = "data/nilai_contoh.txt"
    kkm = 75

    data = baca_data(path, validasi_nilai)

    if not data:
        print("Tidak ada data valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data)
    ketuntasan = hitung_ketuntasan(data, kkm)

    print("=== REKAP NILAI MATEMATIKA ===")
    print(f"Jumlah siswa: {statistik['jumlah_siswa']}")
    print(f"Rata-rata: {statistik['rata_rata']:.2f}")
    print(f"Nilai minimum: {statistik['minimum']}")
    print(f"Nilai maksimum: {statistik['maksimum']}")
    print(f"Siswa tuntas: {ketuntasan['tuntas']}")
    print(f"Siswa belum tuntas: {ketuntasan['belum_tuntas']}")

    simpan_laporan(statistik, ketuntasan, "output/laporan.txt")


if __name__ == "__main__":
    main()