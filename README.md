# Mini Project 2 (DDP)

PRAKTIKUM MINI PROJECT 2 DDP - Sistem Manajemen Stok Cemilan dengan Login dan Hak Akses

Nama : Qonitah Khansa' Ayu Madani Alamsyah<br>
NIM : 2509116113<br>
Kelas: Sistem Informasi C’25

# Flowchart Manajemen Stok Cemilan  
Saya menggunakan 200% zoom agar jpeg flowchart nya HD/tidak buram
![minpro2](https://github.com/user-attachments/assets/38f7738e-54e1-468c-a994-a6f76946b2df)


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

# Output Program
# Login<br>
Saat pertama kali dijalankan, program meminta pengguna memasukkan username dan password.

Jika login benar → muncul pesan sambutan sesuai role.<br>
Jika salah → muncul pesan error “Username atau password salah!”.<br>

(tampilan role pemilik)<br>
<img width="436" height="110" alt="image" src="https://github.com/user-attachments/assets/1f4c043f-0994-4f61-bd11-3a8e37fa6348" />

(tampilan role teman)<br>
<img width="503" height="87" alt="image" src="https://github.com/user-attachments/assets/b72c054b-39bc-433f-9c4f-57e7f01bac49" />

# Tambah Daftar
Pemilik menginput data cemilan baru. Setelah berhasil, muncul konfirmasi.
<img width="538" height="179" alt="image" src="https://github.com/user-attachments/assets/249a48fd-a94b-43ac-bb4e-cb36234fcfad" />

# Lihat Daftar
Menampilkan seluruh cemilan dalam bentuk tabel. Jika kosong → muncul pesan “Belum ada data cemilan.
<img width="503" height="149" alt="image" src="https://github.com/user-attachments/assets/3bfe9345-1622-481c-956a-0a1a2c118309" />

# Ubah Data
Pemilik memilih nomor urut cemilan, lalu mengisi data baru. Kalau input dikosongkan, nilai lama tetap
<img width="668" height="226" alt="image" src="https://github.com/user-attachments/assets/fa16bde9-4db1-40de-9e26-d9538e5a237b" />

# Hapus Data
Pemilik memilih nomor urut cemilan untuk dihapus. Setelah berhasil, muncul konfirmasi.
<img width="563" height="174" alt="image" src="https://github.com/user-attachments/assets/d01a9dc7-66c4-4c10-adc2-0d389e2e7d16" />

# Logout 
Setelah logout, user akan ditanya apakah ingin menutup program.
<img width="467" height="119" alt="image" src="https://github.com/user-attachments/assets/290846ab-dcb7-4986-a5d7-f315c7d7862c" />

# Tujuan Project 
Alasan saya membuat program python ini "Sistem Manajemen Stok Cemilan" karena :<br>
Program ini dibuat sebagai solusi sederhana untuk mencatat stok cemilan agar tidak ada yang lupa, terutama bagi pengguna yang suka nyemil tapi sering lupa status stoknya.<br>
1. Melatih pemahaman konsep CRUD (Create, Read, Update, Delete) pada Python.<br>
2. Menerapkan struktur kontrol (if, while, function) dalam program nyata.<br>
3. Memberikan gambaran sederhana bagaimana sistem login dengan role bekerja.<br>
4. Membantu pengguna mencatat stok cemilan, baik untuk pemilik (full akses) maupun teman (hanya melihat).

# Terima Kasih
