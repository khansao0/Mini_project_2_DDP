# Mini Project 2 (DDP)

PRAKTIKUM MINI PROJECT 2 DDP - Sistem Manajemen Stok Cemilan dengan Login dan Hak Akses

Nama : Qonitah Khansa' Ayu Madani Alamsyah
NIM : 2509116113
Kelas: Sistem Informasi C’25

# Flowchart Sistem Manajemen Stok Cemilan  
Saya menggunakan 200% zoom agar jpeg flowchart nya HD/tidak buram  

Alur Program<br>
1. Login<br>
User masukkan username dan password.<br>Kalau sesuai, login berhasil dan diarahkan ke menu sesuai rolenya.<br>
Kalau salah, diminta ulang.

2. Menu Pemilik<br>
Tambah data cemilan baru.<br>
Lihat daftar cemilan.<br>
Ubah data tertentu.<br>
Hapus data.<br>
Logout untuk kembali ke halaman login.

3. Menu Teman <br>
Hanya bisa lihat daftar cemilan.<br>
Bisa logout untuk kembali ke login.<br>

4. Tutup Program<br>
Setelah logout, user bisa pilih keluar sepenuhnya atau login ulang.<br>

Program ini menerapkan tiga empat proses dasar CRUD (Create, Read, update, Delete):<br>

1. Login<br>
Data akun disimpan dalam dictionary sederhana:<br>
asa → role: Pemilik<br>
imsa → role: Teman

2. Lihat Daftar Cemilan<br>
Menampilkan daftar cemilan dalam bentuk tabel rapi. Kalau belum ada data, keluar pesan “Belum ada data cemilan.”<br>
Tambah Cemilan<br>
Pemilik bisa menambahkan data baru dengan input:<br>
Nama cemilan<br>
Rasa<br>
Jumlah stok<br>
Status (ada / habis / expired)<br>

3. Ubah Cemilan<br>
Pemilik bisa mengedit data yang sudah ada. Kalau user tekan Enter tanpa isi input, data lama tetap dipakai.

4. Hapus Cemilan<br>
Pemilik bisa menghapus cemilan berdasarkan nomor urut. Kalau nomor salah, data tidak akan terhapus.

5. Logout & Keluar<br>
Logout akan kembali ke halaman login.<br>
Setelah logout, user bisa pilih apakah mau keluar program atau lanjut login lagi.

#Output Program

# Login
<img width="436" height="110" alt="image" src="https://github.com/user-attachments/assets/1f4c043f-0994-4f61-bd11-3a8e37fa6348" />

# Tambah Daftar

<img width="538" height="179" alt="image" src="https://github.com/user-attachments/assets/249a48fd-a94b-43ac-bb4e-cb36234fcfad" />

# Lihat Daftar

<img width="503" height="149" alt="image" src="https://github.com/user-attachments/assets/3bfe9345-1622-481c-956a-0a1a2c118309" />

# Ubah Data

<img width="668" height="226" alt="image" src="https://github.com/user-attachments/assets/fa16bde9-4db1-40de-9e26-d9538e5a237b" />

# Hapus Data

<img width="563" height="174" alt="image" src="https://github.com/user-attachments/assets/d01a9dc7-66c4-4c10-adc2-0d389e2e7d16" />

# Logout 

<img width="467" height="119" alt="image" src="https://github.com/user-attachments/assets/290846ab-dcb7-4986-a5d7-f315c7d7862c" />
