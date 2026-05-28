# NOMOR 1:
a = 4
b = 3
print(a == b) #operator ==
print(a != b) #operator !=
print(a > b)  #operator >
print(a < b)  #operator <
print(a >= b) #operator >=
print(a <= b) #operator <=

# NOMOR 2: 
ikan = int(input("masukan angka : "))
print(ikan > 100)

# NOMOR 3:
ikan = 10
if ikan > 1:
    print("ada banyak ikan dikolam")

# NOMOR 4:
ikan = 0
if ikan > 1:
    print("ada banyak ikan dikolam")
if ikan == 0:
    print("tidak ada ikan dikolam")

# NOMOR 5:
IPK = 4
if IPK > 3:
    print("Cumlaude")
else:
    print("memuaskan")

# NOMOR 6:
IPK = 3.5
if IPK >= 3.6:
    print("Cumlaude")
elif IPK >= 3.5:
    print("Sangat memuaskan")
else:
    print("memuaskan")

# NOMOR 7: 
# Membaca 2 angka
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka ke dua: "))

# Memilih angka yang besar
if angka1 > angka2:
    angka_besar = angka1
else:
    angka_besar = angka2

# Print hasil
print("angka yang besar adalah ", angka_besar)

# NOMOR 8:
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka ke dua: "))
angka3 = int(input("Masukkan angka ke tiga: "))

angka_besar = angka1

if angka2 > angka_besar:
    angka_besar = angka2
if angka3 > angka_besar:
    angka_besar = angka3

print("angka yang paling besar adalah", angka_besar)

# NOMOR 9: 
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka ke dua: "))
angka3 = int(input("Masukkan angka ke tiga: "))

angka_besar = max(angka1, angka2, angka3)

print("angka paling besar adalah ", angka_besar)

# NOMOR 10:
pendapatan_perbulan = float(input("Masukkan pendapatan bulanan Anda: "))
pendapatan_pertahun = pendapatan_perbulan * 12

if pendapatan_pertahun > 500000000:
    pajak = pendapatan_pertahun * 0.30
elif pendapatan_pertahun > 250000000:
    pajak = pendapatan_pertahun * 0.25
elif pendapatan_pertahun > 60000000:
    pajak = pendapatan_pertahun * 0.15
else:
    pajak = pendapatan_pertahun * 0.05

print("Pajak penghasilan yang harus anda bayar adalah", pajak, "rupiah")