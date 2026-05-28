#NOMOR 1
def selamat_ulang_tahun(harapan=True):
    print("Tiga...")
    print("Dua...")
    print("Satu...")
    if not harapan:
        return
    print("Selamat ulang tahun!")

selamat_ulang_tahun()

#NOMOR 2
def selamat_ulang_tahun(harapan=True):
    print("Tiga...")
    print("Dua...")
    print("Satu...")
    if not harapan:
        return
    print("Selamat ulang tahun!")

selamat_ulang_tahun(False)

#NOMOR 3
def uang_saku(a, b):
    return a + b

hasil = uang_saku(100000, 50000)
print("Total uang saku: ", hasil)

#NOMOR 4
def uang_saku():
    print("aku boros banget")
    return 0

print("uang sakunya habis")
uang_saku()
print("aku harus mulai hemat")

#NOMOR 5
def fungsi_aneh(x):
    if(x % 2 == 0):
        return True

print(fungsi_aneh(12))
print(fungsi_aneh(15))

#NOMOR 6
def penjumlahan_list(lst):
    s = 0
    for elemen in lst:
        s += elemen
    return s

print(penjumlahan_list([10, 13, 15]))

#NOMOR 7
def penjumlahan_list(lst):
    s = 0
    for elemen in lst:
        s += elemen
    return s

print(penjumlahan_list(7))

#NOMOR 8
def buat_list(n):
    hasil = []
    for i in range(1, n + 1):
        hasil.append(i)
    return hasil

print(buat_list(5))

#NOMOR 9
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "-> ", end="")
    hasil = tahun_kabisat(th)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

#NOMOR 10
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return None

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    th = data_uji[i]
    bln = data_bulan[i]
    print(th, bln, "-> ", end="")
    hasil = hari_didalam_bulan(th, bln)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

#NOMOR 11
def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return None

def hari_pada_tahun(tahun, bulan, hari):
    if bulan < 1 or bulan > 12:
        return None
    max_hari = hari_didalam_bulan(tahun, bulan)
    if hari < 1 or hari > max_hari:
        return None
    
    total = 0
    for b in range(1, bulan):
        total += hari_didalam_bulan(tahun, b)
    total += hari
    return total

print(hari_pada_tahun(2000, 12, 31))

#NOMOR 12
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, " ", end="")
print()

#NOMOR 13
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return False
    return True

for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, " ", end="")
print()

#NOMOR 14
def liter100km_ke_mpg(liter):
    mil = 100000 / 1609.344
    galon = liter / 3.785411784
    return mil / galon

def mpg_ke_liter100km(mpg):
    mil = 100000 / 1609.344
    galon = mil / mpg
    liter = galon * 3.785411784
    return liter

print(liter100km_ke_mpg(3.9))
print(liter100km_ke_mpg(7.5))
print(liter100km_ke_mpg(10.0))
print(mpg_ke_liter100km(39.0))
print(mpg_ke_liter100km(23.5))