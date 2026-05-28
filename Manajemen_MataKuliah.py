# ============================================================
#        PROGRAM MANAJEMEN JADWAL KULIAH & MATA KULIAH
# ============================================================

import os  # modul bawaan Python untuk perintah sistem operasi (dipakai buat clear terminal)

# ======================== DATA AWAL ========================
# List of dict — setiap elemen adalah satu mata kuliah dengan 5 key: mata_kuliah, hari, jam, ruang, sks
jadwal_kuliah = [
    {"mata_kuliah": "Basis Data",              "hari": "Senin",  "jam": "12:00", "ruang": "Lab 2", "sks": 3},
    {"mata_kuliah": "Aljabar Linear",          "hari": "Selasa", "jam": "10:00", "ruang": "F201",  "sks": 3},
    {"mata_kuliah": "Algoritma & Pemrograman", "hari": "Rabu",   "jam": "07:30", "ruang": "Lab 2", "sks": 5},
    {"mata_kuliah": "Struktur Data",           "hari": "Kamis",  "jam": "09:00", "ruang": "Lab 1", "sks": 3},
    {"mata_kuliah": "Logika Informatika",      "hari": "Jumat",  "jam": "11:00", "ruang": "F302",  "sks": 4},
    {"mata_kuliah": "Kalkulus",                "hari": "Jumat",  "jam": "13:00", "ruang": "N302",  "sks": 2},
]

# ======================= FUNGSI UTILITAS =======================

def clear():
    # os.system() menjalankan perintah terminal: 'cls' di Windows, 'clear' di Linux/Mac
    # os.name == 'nt' artinya sistem operasinya Windows
    os.system('cls' if os.name == 'nt' else 'clear')

def garis(karakter="=", panjang=55):
    # Mencetak garis pemisah — karakter default '=' sebanyak 55 kali
    # Parameter bisa diganti, misal garis("-") untuk garis putus-putus
    print(karakter * panjang)

def header(judul):
    # Fungsi ini mencetak judul yang diapit dua garis '=' di atas dan bawah
    garis()
    print(f"  {judul}")
    garis()

def cetak_matkul(daftar, nomor_mulai=1):
    # Mencetak daftar mata kuliah dalam format tabel rata kiri
    # f-string dengan :<N mengatur lebar kolom agar setiap kolom sejajar
    print(f"  {'No':<4} {'Mata Kuliah':<30} {'Hari':<8} {'Jam':<7} {'Ruang':<7} {'SKS'}")
    garis("-")  # garis pemisah header dengan isi tabel
    hari_sebelumnya = None  # menyimpan hari dari baris sebelumnya
    for i, mk in enumerate(daftar):  # enumerate() menghasilkan pasangan (indeks, nilai)
        # Jika hari sama dengan baris sebelumnya, kolom hari dikosongkan agar tidak berulang
        tampil_hari = mk["hari"] if mk["hari"] != hari_sebelumnya else ""
        hari_sebelumnya = mk["hari"]  # update hari terakhir yang sudah dicetak
        print(f"  {nomor_mulai + i:<4} {mk['mata_kuliah']:<30} {tampil_hari:<8} {mk['jam']:<7} {mk['ruang']:<7} {mk['sks']}")

# ======================== FITUR 1 ========================
def tampilkan_semua_jadwal():
    header("📅  FITUR 1 — SEMUA JADWAL KULIAH")

    total = len(jadwal_kuliah)  # len() menghitung jumlah elemen dalam list

    cetak_matkul(jadwal_kuliah)  # tampilkan semua jadwal dalam format tabel
    garis()

    # Perulangan for untuk akumulasi total SKS dari semua mata kuliah
    total_sks = 0
    for mk in jadwal_kuliah:
        total_sks += mk["sks"]  # mk["sks"] mengakses nilai key "sks" dari tiap dict

    print(f"  Total Mata Kuliah : {total}")
    print(f"  Total SKS         : {total_sks}")
    garis()

# ======================== FITUR 2 ========================
def cari_jadwal_per_hari():
    header("🔍  FITUR 2 — CARI JADWAL PER HARI")

    hari_tersedia = []  # list kosong untuk menampung hari yang sudah muncul

    # Perulangan untuk mengumpulkan hari unik (tanpa duplikat)
    for mk in jadwal_kuliah:
        if mk["hari"] not in hari_tersedia:  # cek apakah hari sudah ada di list
            hari_tersedia.append(mk["hari"])  # kalau belum ada, tambahkan

    print("  Hari yang tersedia:")
    for i, h in enumerate(hari_tersedia):  # tampilkan daftar hari bernomor
        print(f"    {i+1}. {h}")

    print()

    # Loop validasi input — terus berulang sampai user memasukkan input yang valid
    # while True artinya loop jalan terus, hanya berhenti kalau ada perintah break
    while True:
        # .strip() hapus spasi di awal/akhir, .capitalize() huruf pertama jadi kapital
        hari_input = input("  Masukkan hari yang ingin dicari: ").strip().capitalize()

        # Validasi 1: .isdigit() mengembalikan True jika semua karakter adalah angka
        # contoh: "1".isdigit() → True, "123".isdigit() → True, "Senin".isdigit() → False
        if hari_input.isdigit():
            print(f"\n  ❌ '{hari_input}' adalah angka, bukan nama hari.")
            print(f"  ➡️  Tolong masukkan nama hari (contoh: Senin, Selasa, Rabu...)\n")
            # tidak ada break → loop kembali ke atas, user diminta input ulang

        # Validasi 2: cek apakah input mengandung karakter selain huruf (misal "Sen1n", "R@bu")
        # .isalpha() mengembalikan True hanya jika semua karakter adalah huruf
        elif not hari_input.isalpha():
            print(f"\n  ❌ '{hari_input}' mengandung karakter tidak valid.")
            print(f"  ➡️  Tolong masukkan nama hari dengan huruf saja (contoh: Senin, Rabu...)\n")
            # tidak ada break → loop kembali ke atas, user diminta input ulang

        # Jika input lolos semua validasi (hanya huruf, bukan angka)
        else:
            break  # keluar dari loop while, lanjut ke proses pencarian

    # List comprehension: buat list baru yang hanya berisi mk dengan hari yang cocok
    # kondisi: mk["hari"] == hari_input → hanya ambil data yang harinya sesuai input
    hasil = [mk for mk in jadwal_kuliah if mk["hari"] == hari_input]

    print()
    # Percabangan: tampilkan pesan sesuai ada/tidaknya hasil pencarian
    if len(hasil) == 0:
        # len(hasil) == 0 berarti tidak ada mata kuliah di hari tersebut
        print(f"  ❌ Tidak ada jadwal untuk hari '{hari_input}'.")
        print(f"  ➡️  Pastikan nama hari sesuai daftar di atas.")
    else:
        # len(hasil) > 0 berarti ditemukan minimal 1 mata kuliah
        print(f"  ✅ Jadwal kuliah hari {hari_input} ({len(hasil)} mata kuliah):")
        garis("-")
        cetak_matkul(hasil)  # cetak hasil pencarian dalam format tabel
    garis()

# ======================== FITUR 3 ========================
def tambah_jadwal():
    header("➕  FITUR 3 — TAMBAH MATA KULIAH BARU")

    print("  Isi data mata kuliah baru:\n")

    # .title() otomatis kapitalisasi huruf pertama tiap kata
    # agar konsisten dengan data yang sudah ada di list (misal "basis data" → "Basis Data")
    nama = input("  Nama Mata Kuliah : ").strip().title()

    # .capitalize() membuat huruf pertama kapital (misal "senin" → "Senin")
    hari = input("  Hari             : ").strip().capitalize()

    # Validasi jam: loop terus sampai format jam valid
    while True:
        jam = input("  Jam (HH:MM)      : ").strip()
        bagian = jam.split(":")  # pisah string berdasarkan titik dua, hasil list 2 elemen
        # cek: harus ada 2 bagian, keduanya angka, jam 0–23, menit 0–59
        if (len(bagian) == 2 and bagian[0].isdigit() and bagian[1].isdigit()
                and 0 <= int(bagian[0]) <= 23 and 0 <= int(bagian[1]) <= 59):
            break  # input valid, keluar dari loop
        print("  ⚠️  Format jam tidak valid! Gunakan HH:MM (contoh: 08:30)")

    # .title() agar huruf awal tiap kata kapital (misal "lab 2" → "Lab 2", "f201" → "F201")
    ruang = input("  Ruang            : ").strip().title()

    # Validasi SKS: loop sampai user memasukkan angka antara 1–6
    while True:
        try:
            sks = int(input("  SKS              : ").strip())  # int() konversi string ke bilangan bulat
            if sks < 1 or sks > 6:
                print("  ⚠️  SKS harus antara 1–6, coba lagi.")
            else:
                break  # angka valid, keluar dari loop
        except ValueError:  # muncul jika input bukan angka (misal huruf)
            print("  ⚠️  SKS harus berupa angka!")

    # Cek duplikat: bandingkan nama baru dengan semua yang ada (case-insensitive dengan .lower())
    duplikat = False
    for mk in jadwal_kuliah:
        if mk["mata_kuliah"].lower() == nama.lower():  # .lower() agar tidak peka huruf besar/kecil
            duplikat = True
            break  # langsung berhenti kalau sudah ketemu duplikat

    if duplikat:
        print(f"\n  ❌ Mata kuliah '{nama}' sudah ada di jadwal!")
    else:
        # Tambahkan dict baru ke dalam list jadwal_kuliah menggunakan .append()
        jadwal_kuliah.append({
            "mata_kuliah": nama,
            "hari": hari,
            "jam": jam,
            "ruang": ruang,
            "sks": sks
        })
        print(f"\n  ✅ '{nama}' berhasil ditambahkan!")
        print(f"  Total sekarang: {len(jadwal_kuliah)} mata kuliah.")
    garis()

# ======================== FITUR 4 ========================
def urutkan_jadwal():
    header("📊  FITUR 4 — URUTKAN JADWAL KULIAH")

    print("  Urutkan berdasarkan:")
    print("    1. Hari")
    print("    2. Jam")
    print("    3. SKS (terbesar ke terkecil)")
    print("    4. Nama Mata Kuliah (A–Z)")
    print()

    pilihan = input("  Pilih (1-4): ").strip()

    # sorted() mengembalikan list baru yang sudah diurutkan tanpa mengubah list asli
    # key= menentukan nilai yang dipakai sebagai acuan urutan
    # lambda adalah fungsi anonim (tanpa nama), x mewakili setiap elemen list
    if pilihan == "1":
        urutan_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
        # .index() cari posisi hari di urutan_hari; kalau tidak ditemukan pakai angka 99 (paling belakang)
        hasil_sort = sorted(jadwal_kuliah, key=lambda x: urutan_hari.index(x["hari"]) if x["hari"] in urutan_hari else 99)
        judul_sort = "berdasarkan Hari"
    elif pilihan == "2":
        # Jam dalam format HH:MM bisa diurutkan sebagai string karena formatnya konsisten
        hasil_sort = sorted(jadwal_kuliah, key=lambda x: x["jam"])
        judul_sort = "berdasarkan Jam"
    elif pilihan == "3":
        # reverse=True → urutan terbesar ke terkecil
        hasil_sort = sorted(jadwal_kuliah, key=lambda x: x["sks"], reverse=True)
        judul_sort = "berdasarkan SKS (terbesar)"
    elif pilihan == "4":
        # Urutan alfabetis default Python (A–Z)
        hasil_sort = sorted(jadwal_kuliah, key=lambda x: x["mata_kuliah"])
        judul_sort = "berdasarkan Nama (A–Z)"
    else:
        print("  ❌ Pilihan tidak valid.")
        return  # keluar dari fungsi jika input tidak valid

    print(f"\n  ✅ Jadwal diurutkan {judul_sort}:\n")
    cetak_matkul(hasil_sort)
    garis()

# ======================== MENU UTAMA ========================
def menu_utama():
    while True:  # loop tak terbatas, berhenti hanya jika user pilih 0
        clear()
        header("🎓  SISTEM MANAJEMEN JADWAL KULIAH")
        print("  1. 📅  Tampilkan Semua Jadwal")
        print("  2. 🔍  Cari Jadwal Per Hari")
        print("  3. ➕  Tambah Mata Kuliah Baru")
        print("  4. 📊  Urutkan Jadwal Kuliah")
        print("  0. 🚪  Keluar")
        garis()

        pilihan = input("  Pilih menu (0-4): ").strip()
        print()

        # Percabangan untuk memanggil fungsi sesuai pilihan user
        if pilihan == "1":
            tampilkan_semua_jadwal()
        elif pilihan == "2":
            cari_jadwal_per_hari()
        elif pilihan == "3":
            tambah_jadwal()
        elif pilihan == "4":
            urutkan_jadwal()
        elif pilihan == "0":
            clear()
            print("  👋 Terima kasih! Semangat kuliahnya!\n")
            break  # keluar dari loop while → program selesai
        else:
            print("  ⚠️  Pilihan tidak valid, coba lagi.\n")

        input("  Tekan Enter untuk kembali ke menu...\n")  # jeda sebelum layar di-clear

# ======================== JALANKAN ========================
# Blok ini hanya jalan kalau file dijalankan langsung (bukan di-import dari file lain)
if __name__ == "__main__":
    menu_utama()
