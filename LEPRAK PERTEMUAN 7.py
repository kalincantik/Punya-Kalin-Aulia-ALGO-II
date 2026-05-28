#nomor 1
angka = [20, 7, "ikan", 5, 6]
print("isi dari list awal:", angka) #print isi list dri awal

angka[0] = 207
print("isi dari list baru:", angka) #isi dari list yang sudah diubah

angka[2] = angka[4] #ngecopy isi elemen5 ke elemen3(diganti)
print("isi dari list sekarang:", angka) #print isi list terbaru

#nomor 2
angka = [20, 7, "ikan", 5, 6]
print(angka[2]) #mengakses elemen pertama list

angka = [20, 7, "ikan", 5, 6]
print(angka) #ngeprint  semua isi list

#nomor 3
ngka = [20, 7, "ikan", 5, 6]
print('Panjang list: ', len(angka)) #ngeprint panjang listnya

#nomor 4
angka = [20, 7, "ikan", 5, 6]
del angka[2]
print(len(angka))
print(angka)

print(angka[4])
angka[4] = 1

#nomor 5
angka = [20, 23, 5, 6]
print(angka[-4])

#nomor 6
topi_list = [1, 2, 3, 4, 5]
topi_list[2] = int(input('masukin disini angkanya: '))

del topi_list[4]

print(len(topi_list))

print(topi_list)

#nomor 7
angka = [111, 7, 2, 1]
print(len(angka))
print(angka)

###

angka.append(4)

print(len(angka))
print(angka)

###

angka.insert(0, 222)
print(len(angka))
print(angka)

angka.insert(1, 333) # Tambahkan nilai 333 pada index ke-1
print(len(angka)) # Print panjang listnya
print(angka) # Print isi listnya
 
#nomor 8
my_list = []  

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#nomor 9
my_list = []  

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

#nomor 10
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#nomor 11
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)
#nomor 12
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

#menggunakan for
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

#nmor 13
#langkah 1
exo = []
print('langkah 1: ', exo)

#langkah 2
exo.append('suho')
exo.append('kai')
exo.append('chanyeol')
exo.append('sehun')
print('langkah 2: ', exo)

#langkah 3
tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for anggota in tambahan:
    exo.append(anggota)
print("langkah 3: ", exo)

#langkah 4
del exo[6]
del exo[7]
del exo[7]
print("langkah 4: ", exo)

#langkah 5
exo.insert(len(exo)-2, "xiumin")
print("langkah 5: ", exo)