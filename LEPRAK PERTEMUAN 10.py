# NOMOR 1
koleksi = ["Kalin", "Cindy", "Wafa", "Ica", "Achel"]
# Hanya mengambil nama yang mengandung huruf 'a'
koleksi_ada_a = [k for k in koleksi if 'a' in k]
print(koleksi_ada_a)

# NOMOR 2
nilai_siswa = [
    [80, 90],
    [70, 85],
    [95, 88]
]
print(nilai_siswa)

# NOMOR 3
list = [
    ["kaonho", "mancing"],
    ["yeoljun", "badminton"]
]
hobi_kaonho = list[0][1]
hobi_yeoljun = list[1][1]
print(hobi_kaonho)
print(hobi_yeoljun)

# NOMOR 4
def sapa_idol(nama):
    print("halo " + nama + " !")

sapa_idol("kaonho")
sapa_idol("yeoljun")

# NOMOR 5
hasil = [i * 3 for i in range(1, 11) if i % 2 == 0]
print(hasil)

# NOMOR 6
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for baris in array:
    for angka in baris:
        print(angka, end=" ")
    print()

# NOMOR 7
data = [[1, 4], [8, 9], [10, 11]]
flat = [angka for baris in data for angka in baris]
print(flat)

# NOMOR 8
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

hasil = luas_persegi_panjang(8, 5)
print("Luas:", hasil)