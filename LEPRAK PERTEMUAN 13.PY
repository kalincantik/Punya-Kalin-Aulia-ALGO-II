#NOMOR 1
tuple_1 = (1, 2, 3)
tuple_2 = 4, 5, 6
tuple_kosong = ()
print(tuple_1)
print(tuple_2)
print(tuple_kosong)

#NOMOR 2
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[:1])
print(my_tuple[:-2])

for element in my_tuple:
    print(element)

#NOMOR 3
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

my_tuple.append(6)
print(my_tuple)

del my_tuple
print(my_tuple)

my_tuple [1] = -10
print(my_tuple)

#NOMOR 4
my_tuple = (1, 2, 3, 4, 5)
t1 = my_tuple + (6, 5)
t2 = my_tuple * 2

print(len(2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#NOMOR 5
pribumi = [("ucup", 123), ("robi", 456), ("kalin", 789), ("abil", 999)]
for nama, nomer in pribumi:
    print(f"Nama: {nama}, Nomer: {nomer}")

#NOMOR 6, 7 DAN 8
class Nomer:
    def __init__(self):
        self.lis = {}

class Child(Nomer):
    def __init__(self):
        super().__init__()

    def tambah(self, nama, nomer):
        self.lis[nama] = nomer

    def akses(self, nama):
        if nama in self.lis:
            print(f"Ketemu! Nomer {nama} adalah: {self.lis[nama]}")
            return True
        return False

    def metod(self):
        for nama in self.lis.keys():
            return nama

    def cetak(self):
        print(f"Hasilnya: {self.lis}")

#nomor 6 wir
pribumi = [("ucup", 123), ("robi", 456), ("kalin", 789), ("abil", 999)]
objek = []

for nama, nomer in pribumi:
    obj = Child()
    obj.tambah(nama, nomer)
    objek.append(obj)

for orang in objek:
    orang.cetak()

#nomor 7 wir
tayo = input("Masukkan nama kontak: ")
ketemu = False

for orang in objek:
    if orang.akses(tayo):
        ketemu = True
        break

if not ketemu:
    print(f"Yah, '{tayo}' nggak ada di kontak wir!")

#nomor 8 wir
kontak = []
for orang in objek:
    haha = orang.metod()
    kontak.append(haha)
print(f"Kontak versi keys: {kontak}")

#NOMOR 9
nilai = {"kalin" : 85, "yusuf" : 90, "abil" : 95, "hamdi" : 80}

for angka in nilai.values():
    print(angka)

#NOMOR 10
idol = {"cortis" : "martin", "txt" : "soobin", "nct dream" : "marklee"}
for grup, leader in idol.items():
    print(grup, "leadernya adalah", leader)

#NOMOR 11
idol = {"cortis" : "martin", "txt" : "soobin", "nct dream" : "marklee"}

idol.update({"exo" : "suho"})

for grup, leader in idol.items():
    print(grup, "leadernya adalah", leader)

#NOMOR 12
X = {"1": "saya", "2": "kamu", "3": "dia"}
print(X.popitem())

#NOMOR 13
x = {"1": ["saya"], "2": ["bareng"], "3": ["temen"]}

x["1"].append("lagi")
x["4"] = ["kelas"]
print(x)
del x["4"]
print(x)

#NOMOR 14
menu = {1: "tambah data", 2: "lihat data", 3: "keluar"}

try:
    pilihan = int(input("pilih menu (1-3): "))
    if pilihan not in menu:
        raise ValueError("menu tidak tersedia")
    print(f"kamu memilih: {menu[pilihan]}")

except ValueError as e:
    print(f"error: {e}")

#NOMOR 15
data = {"nama": "brata", "umur": 20}

try:
    pilihan = int(input("pilih (1=nama, 2=umur, 3=nilai):"))
    kunci =["nama", "umur", "nilai"] [pilihan - 1]
    hasil = int(data[kunci]) + 5
    print(f"hasil: {hasil}")

except ValueError:
    print("innput bukan angka!")
except KeyError:
    print("data tidak ditemukan!")
except IndexError:
    print("pilihan di luar menu!")
    