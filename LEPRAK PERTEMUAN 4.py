# NOMOR 1:
print("Whats your name?")
nama = input()
print("Hello!", nama, "how are you?")

# NOMOR 2: 
umur = input("how old are you? ")
print(umur, "y.o")

# NOMOR 3:
umur = input("how old are you? ")
umurbaru = umur + 2
print("now", umurbaru, "y.o")

# NOMOR 4:
score = float(input("berapa score kamu? "))
myscore = score ** 2.0
print("before: ", score, " after: ", myscore)

# NOMOR 5:
leg_a = float(input("input first leg length: "))
leg_b = float(input("input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("hypotenuse length is", hypo)

# NOMOR 6:
leg_a = float(input("input first leg length: "))
leg_b = float(input("input second leg length: "))
print("hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# NOMOR 7:
frstorder = input("What would you like to order? ")
secorder = input("Anything else? ")
print("Thank you.")
print("\nYour order is " + frstorder + " " + "and" + " " + secorder + ".")

# NOMOR 8:
print("*" * 6 + " " + "*")
print(" " * 2 + "^" + " ")
print("*" * 6 + " " + "*")
print(3 * "kalin\n")

# NOMOR 9:
leg_a = float(input("input first leg length: "))
leg_b = float(input("input second leg length: "))
print("hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# NOMOR 10:l
x = input("enter a number : ")
print(type(x))

# NOMOR 11: 
a = int(input("masukan angka pertama: "))
b = int(input("masukan angka kedua: "))

jumlah = a + b
kurang = a - b
kali = a * b
bagi = a / b

print("\nhasil penjumlahan: ", jumlah)
print("hasil pengurangan: ", kurang)
print("hasil perkalian: ", kali)
print("hasil pembagian: ", bagi)
print("\nselamat kamu sudah pintar matematika")

# NOMOR 12:
x = float(input("masukan angka x: "))
y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x)))
print("hasil dari variabel y adalah: ", y)

# NOMOR 13:
jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

menit = menit + durasi
jam = jam + menit // 60
menit = menit % 60

print("acara selesai pada pukul: ", jam, ":", menit)