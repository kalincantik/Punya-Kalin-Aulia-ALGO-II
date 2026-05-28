#NOMOR 1
def nilaiasli(x):
    nilaitambahan = 20
    return x + 20

print("total nilai:", nilaiasli(80))
print(nilaitambahan)

#NOMOR 2
bilangan = 3
def modulo_bilangan(x):
    return x % bilangan

print(modulo_bilangan(19))

#NOMOR 3
def penguarangan(x):
    bilangan = 9
    return x - bilangan

bilangan = 3
print(penguarangan(99))

#NOMOR 4
bilangan = 2
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 3
    return bilangan

print(return_bilangan())
print(bilangan)

#NOMOR 5
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi * tinggi)
    return imt

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

if index_massa_tubuh < 25.0:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[0])
elif 25.0 <= index_massa_tubuh <= 27.0:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[1])
else:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[2], ". Anda harus diet!")

#NOMOR 6
def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(cek_segitiga(1, 1, 1)) 
print(cek_segitiga(1, 1, 3)) 

#NOMOR 7
def cek_segitiga(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 1, 3))

#NOMOR 8
def cek_segitiga(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 1, 3))

#NOMOR 9
def faktorial(n):
    if n < 0:
        return None

    if n < 2:
        return 1

    hasil = 1

    for i in range(1, n + 1):
        hasil = hasil * i
    
    return hasil

n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! = ", faktorial(n))

#NOMOR 10
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    hasil_jumlah = 0

    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2
        elem_1 = elem_2 
        elem_2 = hasil_jumlah
        
    return hasil_jumlah

for n in range(1, 16):
    print(n, "->", fibonacci(n))

#NOMOR 11
def faktorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * faktorial(n - 1)

print(faktorial(5))

#NOMOR 12
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))