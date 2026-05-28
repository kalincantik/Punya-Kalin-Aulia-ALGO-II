#nomor 1
while True:
    print("kalin cantik banget")

#nomor 2
counter = 9
while counter >= 3:
    print (counter)
    counter -= 3

#nomor 3
#membuat variabel angka ganjil dan angka genap
angka_genap = 0
angka_ganjil = 0

#membaca angka pertama
angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

while angka != 0: #cek apakah angka tidak sama dengan 0
    if angka % 2 == 1: #mengecek apakah sisa bagi angka dengan 2 adalah 1
        angka_ganjil += 1
    else:
        angka_genap += 1

    #membaca angka selanjutnya
    angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

#menampilkan total angka ganjil dan angka genap
print("Jumlah Angka Ganjil: ", angka_ganjil)
print("Jumlah Angka Genap: ", angka_genap)

#nomor 4
secret_number = 207

print("""
+=======================================+
| Welcome to my game, muggle!           |
| Ayo masukin angka nya dan tebak       |
| angka berapa yang kalin pilih         |
| buat kamu^-^.                         |
| Berapa nih angka rahasianya bestie?   |
+=======================================+
""")

angka = int(input('masukin angkanya disini bestie: '))

while angka != secret_number:
    print('tetot salah! kamu nyangkut deh di Loop aku')
    angka = int(input('masukin angkanya lagi bestie: '))

print('yeyyyy Selamat, Muggle! kamu bebas sekarang!')

#nomor 5
for a in range(8):
    print("nilai a saat ini adalah", a) 
print()
for b in range(3,9):
    print("nilai b saat ini adalah", b)
print()
for c in range(3,9,3):
    print("nilai c saat ini adalah", c)
print()
for d in range(3,3):
    print("nilai d saat ini adalah", d)
print()
for e in range(3,2):
    print("nilai e saat ini adalah", e)

#nomor 6
power = 1
for expo in range(5):
    print('2 pangkat', expo, "adalah", power)
    power *= 2

#nomor 7
# Contoh break
print("kategori nilai B:")
for i in range(7,10):
    if i == 9:
        break
    print("Nilai B : ", i)
print("diatas angka 9 A")

# Contoh continue
print("\nInstruksi continue:")
for i in range(1,10):
    if i == 3 or i == 7:
        continue
    print("Bagian ini ada di dalam loop.", i)
print("Bagian ini ada di luar loop.")

#nomor 8
angka_rahasia = 7

print("selamat datang")
print("di game tebak angka")
print("pesulap kalin cantik^^\n")

tebakan = int(input('tebak angka dari 1-10 mana angka istimewa? : '))

while True:
    if tebakan == angka_rahasia:
        print("yeyy tebakanmu betul")
        break
    else:
        print("yahh salahh nihh")
        tebakan = int(input("tebak lagi: "))
#nomor 9
user_word = input('Masukan kata disini :')
user_word = user_word.upper()

for kata in user_word:
    if kata == 'I' or kata == 'O' or kata == 'A' or kata == 'E' or kata == 'U':
     continue
    else:
       print(kata)

#nomor 10
i = 6                           #contoh 1
while i < 10:
    print(i)
    i += 1
else:
    print("else:", i)

i = 6                           #contoh 2
while i < 6:
    print(i)
    i += 1
else:
    print("else:", i)

#nomor 11
for i in range(8):              #contoh 1
    print(i)
else:
    print("else:", i)

i = 111                         #contoh 2
for i in range(6, 5):
    print(i)
else:
    print("else:", i)

#nomor 12
mahasiswa_uin = True
prodi_informatika = False

print(mahasiswa_uin and prodi_informatika)
print(mahasiswa_uin or prodi_informatika)
print(not prodi_informatika)

#nomor 13
i = 20     #biner 10100
j = 23     #biner 10111 

log = i and j
print(log)

bit = i & j
print(bit)

logneg = not i
print(logneg)

bitneg = ~i
print(bitneg)

#nomor 14
a = 5   # biner: 0101

print(a << 1)   # geser kiri 1 kali
print(a << 2)   # geser kiri 2 kali
print(a >> 1)   # geser kanan 1 kali
print(a >> 2)   # geser kanan 2 kali

#nomor 15
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)