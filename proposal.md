# PROPOSAL PROYEK PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

## 1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python.

## 2. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan yang dilakukan oleh guru dalam proses pembelajaran. Pengolahan tersebut meliputi pemeriksaan nilai, perhitungan rata-rata, penentuan nilai tertinggi dan terendah, serta penentuan ketuntasan belajar siswa.

Apabila pengolahan dilakukan secara manual, proses tersebut dapat membutuhkan waktu dan berisiko menimbulkan kesalahan perhitungan. Oleh karena itu, diperlukan program sederhana yang dapat membantu guru mengolah data nilai secara otomatis.

Proyek ini dirancang menggunakan bahasa pemrograman Python dengan antarmuka terminal atau console. Program akan membaca data nilai dari file, melakukan validasi, menghitung statistik, menentukan status ketuntasan, dan menyimpan hasilnya ke dalam file laporan.

## 3. Pengguna dan Tujuan

### A. Pengguna

Pengguna utama program adalah guru matematika yang membutuhkan bantuan untuk mengolah nilai siswa.

### B. Tujuan

1. Membantu guru membaca dan mengolah data nilai siswa.
2. Mengurangi kesalahan dalam perhitungan statistik nilai.
3. Mempermudah penentuan ketuntasan belajar berdasarkan KKM.
4. Menghasilkan laporan nilai yang tersimpan dalam file teks.

## 4. Ruang Lingkup Proyek

### A. Fitur Wajib

1. Membaca data nilai siswa dari file teks.
2. Memvalidasi nilai agar berada dalam rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
5. Menyimpan hasil analisis ke dalam file laporan.

### B. Batasan Proyek

1. Program menggunakan bahasa Python.
2. Program dijalankan melalui terminal atau console.
3. Data masukan disimpan dalam file teks.
4. Nilai siswa harus berupa angka dalam rentang 0–100.
5. KKM ditetapkan sebesar 75 sebagai nilai contoh dan dapat diubah sesuai kebutuhan.
6. Program tidak menggunakan basis data, antarmuka web, atau layanan eksternal.
7. Data yang digunakan untuk pengujian merupakan data contoh, bukan data pribadi siswa yang sebenarnya.

## 5. Analisis Kebutuhan

### A. Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Program dapat membaca data nilai dari file. | Wajib |
| F02 | Program dapat memvalidasi nilai 0–100. | Wajib |
| F03 | Program dapat menghitung rata-rata, minimum, dan maksimum. | Wajib |
| F04 | Program dapat menentukan status ketuntasan berdasarkan KKM. | Wajib |
| F05 | Program dapat menyimpan laporan hasil analisis. | Wajib |

### B. Kebutuhan Nonfungsional

1. Program mudah dijalankan melalui terminal VS Code.
2. Nama variabel dan fungsi mudah dipahami.
3. Pesan kesalahan disampaikan dengan jelas.
4. Program dapat diuji menggunakan data yang sama.
5. Struktur program dibuat modular agar mudah diperbaiki dan dikembangkan.

## 6. Spesifikasi Input, Proses, dan Output (IPO)

| Komponen | Keterangan |
|---|---|
| Input | File teks berisi nama dan nilai siswa serta nilai KKM. |
| Proses | Membaca data, memvalidasi nilai, menghitung statistik, dan menentukan ketuntasan. |
| Output | Rata-rata nilai, nilai minimum, nilai maksimum, jumlah siswa tuntas, jumlah siswa belum tuntas, dan file laporan. |

### Contoh Input

File `nilai_contoh.txt` berisi:

Ayu,85
Budi,78
Citra,90
Dinda,65
Eko,75

KKM yang digunakan adalah 75.

### Contoh Output yang Diharapkan

Jumlah siswa: 5
Rata-rata nilai: 78.60
Nilai minimum: 65
Nilai maksimum: 90
Jumlah siswa tuntas: 4
Jumlah siswa belum tuntas: 1

Keterangan: Siswa dinyatakan tuntas apabila nilainya lebih besar dari atau sama dengan KKM.

## 7. Algoritma dan Pseudocode

MULAI

1. Tentukan lokasi file data dan nilai KKM.
2. Baca data nilai dari file.
3. Jika file tidak ditemukan, tampilkan pesan kesalahan dan hentikan program.
4. Periksa format setiap baris data.
5. Periksa apakah nilai berupa angka dalam rentang 0–100.
6. Simpan data yang valid dan berikan informasi untuk data yang tidak valid.
7. Jika tidak ada data valid, tampilkan pesan bahwa data tidak dapat dianalisis.
8. Hitung jumlah siswa dan rata-rata nilai.
9. Tentukan nilai minimum dan maksimum.
10. Hitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
11. Tampilkan hasil analisis ke terminal.
12. Simpan hasil analisis ke dalam file laporan.
13. Tampilkan pesan bahwa laporan berhasil disimpan.

SELESAI

## 8. Struktur Program dan Modularisasi

Program dibagi menjadi beberapa file berdasarkan tanggung jawabnya.

| File | Fungsi |
|---|---|
| `main.py` | Mengatur alur utama program. |
| `data_io.py` | Membaca data nilai dan menyimpan laporan. |
| `analisis.py` | Menghitung statistik dan ketuntasan siswa. |
| `utilitas.py` | Memvalidasi nilai dan membantu pemeriksaan data. |

Pembagian ini bertujuan agar setiap bagian program memiliki tanggung jawab yang jelas sehingga lebih mudah diuji dan diperbaiki.

## 9. Struktur Data

Struktur data yang digunakan meliputi:

1. List, untuk menyimpan kumpulan nilai siswa.
2. Dictionary, untuk menyimpan data setiap siswa berdasarkan atribut seperti nama dan nilai.
3. String, untuk menyusun pesan dan laporan.
4. File teks, untuk menyimpan data masukan dan hasil laporan.

Contoh model data:

data_siswa = [
    {"nama": "Ayu", "nilai": 85},
    {"nama": "Budi", "nilai": 78},
    {"nama": "Citra", "nilai": 90}
]

Struktur tersebut memudahkan program mengakses nama dan nilai setiap siswa serta melakukan perhitungan statistik.

## 10. Test Case

Pengujian awal dirancang untuk memeriksa kondisi normal, batas, dan input tidak valid.

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 dan program menampilkan statistik dengan benar. |
| TC02 | Batas | Nilai 0 | Nilai diterima sebagai nilai valid. |
| TC03 | Batas | Nilai 100 | Nilai diterima sebagai nilai valid. |
| TC04 | Invalid | Nilai 105 | Nilai ditolak karena berada di luar rentang yang diizinkan. |
| TC05 | Invalid | File data tidak ditemukan | Program menampilkan pesan kesalahan dan tidak berhenti secara tidak terkendali. |
| TC06 | Normal | Nilai 75, 80, 90 dengan KKM 75 | Tiga siswa dinyatakan tuntas. |
| TC07 | Invalid | File tersedia, tetapi tidak berisi data valid | Program menampilkan pesan bahwa tidak ada data yang dapat dianalisis. |

## 11. Pembagian Tugas

Pembagian berikut merupakan contoh dan perlu disesuaikan dengan jumlah serta nama anggota kelompok.

| Peran | Tanggung Jawab | Hasil Pekerjaan |
|---|---|---|
| Koordinator | Mengatur ruang lingkup, mengoordinasikan pekerjaan, dan memeriksa integrasi. | Proposal dan koordinasi proyek. |
| Programmer Data I/O | Merancang pembacaan data dan penyimpanan laporan. | `data_io.py` |
| Programmer Logika | Merancang perhitungan statistik dan ketuntasan. | `analisis.py` |
| Tester/QA | Menyusun dan menguji skenario pengujian. | `tests/test_case.md` |
| Dokumentasi | Menyusun petunjuk penggunaan dan dokumentasi proyek. | `README.md` |

Nama anggota dan penanggung jawab setiap tugas akan ditentukan berdasarkan kesepakatan kelompok. Untuk kelompok kecil, seorang anggota dapat memegang lebih dari satu peran.

## 12. Jadwal Pengerjaan

| Tahap | Kegiatan | Target |
|---|---|---|
| Pertemuan 14 | Menentukan masalah, menyusun proposal, pseudocode, struktur folder, test case, dan pembagian tugas. | Rancangan proyek selesai. |
| Antara Pertemuan 14–15 | Membuat implementasi awal fitur wajib. | Kode awal tersedia. |
| Pertemuan 15 | Mengintegrasikan modul, melakukan pengujian, memperbaiki kesalahan, dan melengkapi dokumentasi. | Program berjalan dan diuji. |
| Pertemuan 16 | Mempresentasikan dan mendemonstrasikan proyek. | Proyek siap dievaluasi. |

## 13. Repository GitHub

Nama repository: `proyek-akhir-analisis-nilai`

URL repository: https://github.com/Maugyu/proyek-akhir-Maulyditha-Revania-Aprilliyanti-Kelompok-3.git

Repository digunakan untuk menyimpan proposal, dokumentasi, struktur program, test case, dan perkembangan implementasi. Setiap perubahan penting dicatat melalui commit agar perkembangan pekerjaan dapat ditelusuri.

## Penutup

Proyek Program Rekap dan Analisis Nilai Matematika Kelas dirancang untuk membantu pengolahan nilai siswa secara sederhana dan sistematis. Melalui penggunaan Python, program diharapkan dapat menghasilkan perhitungan statistik dan informasi ketuntasan secara konsisten.

Rancangan ini menjadi dasar implementasi, pengujian, dan dokumentasi proyek pada pertemuan berikutnya.
