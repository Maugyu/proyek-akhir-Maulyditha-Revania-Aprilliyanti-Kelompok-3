# TEST CASE PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA

## Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca data, memvalidasi nilai, menghitung statistik, menentukan ketuntasan, dan menangani kesalahan.

## TC01 – Perhitungan Statistik Normal

Input:
- Nilai: 80, 70, 90

Hasil yang diharapkan:
- Rata-rata: 80
- Minimum: 70
- Maksimum: 90

## TC02 – Nilai Minimum

Input:
- Nilai: 0

Hasil yang diharapkan:
- Nilai diterima karena berada dalam rentang 0–100.

## TC03 – Nilai Maksimum

Input:
- Nilai: 100

Hasil yang diharapkan:
- Nilai diterima karena berada dalam rentang 0–100.

## TC04 – Nilai Melebihi Batas

Input:
- Nilai: 105

Hasil yang diharapkan:
- Nilai ditolak.
- Program memberikan informasi bahwa nilai harus berada dalam rentang 0–100.

## TC05 – File Tidak Ditemukan

Kondisi:
- File masukan tidak tersedia pada lokasi yang ditentukan.

Hasil yang diharapkan:
- Program menampilkan pesan bahwa file tidak ditemukan.
- Program menangani kesalahan dengan baik.

## TC06 – Pengujian Ketuntasan

Input:
- Nilai: 75, 80, 90
- KKM: 75

Hasil yang diharapkan:
- Jumlah siswa tuntas: 3.
- Jumlah siswa belum tuntas: 0.

## TC07 – Tidak Ada Data Valid

Kondisi:
- File tersedia, tetapi seluruh data kosong atau tidak memenuhi format yang ditentukan.

Hasil yang diharapkan:
- Program menampilkan pesan bahwa tidak ada data valid untuk dianalisis.
- Program tidak menghasilkan statistik yang menyesatkan.