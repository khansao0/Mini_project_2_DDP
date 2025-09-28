# Nama  = Qonitah Khansa' Ayu Madani Alamsyah
# NIM   = 2509116113
# Kelas = Sistem Informasi C'25
# PRAKTIKUM MINI PROJECT 2 - Manajemen Cemilan

# Data login
akun = {
    "asa": {"pw": "123", "role": "Pemilik"},
    "imsa": {"pw": "123", "role": "Teman"}
}

# Stok cemilan
stok = []

# --- Fungsi ---
def login():
    print("="*40)
    print("Sistem Stok Cemilan Asa")
    print("="*40)
    while True:
        user = input("Username: ")
        pw   = input("Password: ")
        if user in akun and akun[user]["pw"] == pw:
            print(f"Halo {user}, login sebagai {akun[user]['role']}\n")
            return akun[user]['role']
        else:
            print("Username atau password salah!\n")

# READ
def lihat():
    print("\n--- DAFTAR CEMILAN ---")
    if stok == []:
        print("Belum ada data cemilan.")
    else:
        print("No | Nama        | Rasa   | Jumlah | Status")
        nomor = 1
        for cemilan in stok:
            print(f"{nomor:<2} | {cemilan['nama']:<10} | {cemilan['rasa']:<6} | {cemilan['jumlah']:<6} | {cemilan['status']}")
            nomor += 1

# CREATE
def tambah():
    nama   = input("Nama cemilan: ")
    rasa   = input("Rasa: ")
    jumlah = input("Jumlah: ")
    status = input("Status: ")
    stok.append({"nama": nama, "rasa": rasa, "jumlah": jumlah, "status": status})
    print("Cemilan berhasil ditambahkan!\n")

# UPDATE
def ubah():
    lihat()
    if stok != []:
        no = int(input("Nomor cemilan yang mau diubah: "))
        if no >= 1 and no <= len(stok):
            cemilan = stok[no-1]
            cemilan["nama"]   = input("Nama baru: ") or cemilan["nama"]
            cemilan["rasa"]   = input("Rasa baru: ") or cemilan["rasa"]
            cemilan["jumlah"] = input("Jumlah baru: ") or cemilan["jumlah"]
            cemilan["status"] = input("Status baru: ") or cemilan["status"]
            print("Data berhasil diubah!\n")

# DELETE
def hapus():
    lihat()
    if stok != []:
        no = int(input("Nomor cemilan yang mau dihapus: "))
        if no >= 1 and no <= len(stok):
            print(f"{stok[no-1]['nama']} dihapus dari daftar.")
            stok.pop(no-1)

# --- Menu ---
def menu_pemilik():
    while True:
        print("\n--- MENU PEMILIK ---")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Ubah")
        print("4. Hapus")
        print("5. Logout")
        pilih = input("Pilih: ")
        if pilih == "1":
            tambah()
        elif pilih == "2":
            lihat()
        elif pilih == "3":
            ubah()
        elif pilih == "4":
            hapus()
        elif pilih == "5":
            break

def menu_teman():
    while True:
        print("\n--- MENU TEMAN ---")
        print("1. Lihat")
        print("2. Logout")
        pilih = input("Pilih: ")
        if pilih == "1":
            lihat()
        elif pilih == "2":
            break

while True:
    role = login()
    if role == "Pemilik":
        menu_pemilik()
    else:
        menu_teman()

    keluar = input("Tutup program? (y/n): ").lower()
    if keluar == "y":
        print("Sampai jumpa!")
        break
