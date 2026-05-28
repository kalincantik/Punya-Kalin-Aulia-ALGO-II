# nomor 1
List = [10, 20, 17, 23, 15]
swapped = True

while swapped:
    swapped = False
    for i in range(len(List) - 1):
        if List[i] > List[i + 1]:
            swapped = True
            List[i], List[i + 1] = List[i + 1], List[i]

print(List)

# nomor 2
List = []
swapped = True
num = int(input("Masukin panjang elemen list yang mau diurutin: "))

for i in range(num):
    val = float(input("Masukin elemen list: "))
    List.append(val)

while swapped:
    swapped = False
    for i in range(len(List) - 1):
        if List[i] > List[i + 1]:
            swapped = True
            List[i], List[i + 1] = List[i + 1], List[i]

print("\nSorted:")
print(List)

# nomor 3
#method short
listeu = [23, 25, 50, 16, 3]
listeu.sort()
print(listeu)


# nomor 4
#method reserve
listt = [10, 25, 30, 15]
listt.reverse()
print(listt)

# nomor 5
list_1 = [1, 3]
list_2 = list_1
list_1[1] = 9
print(list_2)

# nomor 6
listeu = [10, 20, 30, 40, 50, 60, 70]
newlisteu = listeu[2:5]
print(newlisteu)

# nomor 7
listeu = [10, 20, 30, 40, 50, 60, 70]
newlisteu = listeu[2:-2]
print(newlisteu)

# nomor 8
listeu = [10, 20, 30, 40, 50, 60, 70]
newlisteu = listeu[-2:3]
print(newlisteu)

# nomor 9
listeu = [10, 20, 30, 40, 50, 60, 70]
newlisteu = listeu[:3]
print(newlisteu)

# nomor 10
listeu = [10, 20, 30, 40, 50, 60, 70]
newlisteu = listeu[4:]
print(newlisteu)

# nomor 11
listeu = [10, 20, 30, 40, 50, 60, 70]
newlisteu = listeu[:]
print(newlisteu)

# nomor 12
listeu = [10, 20, 30, 40, 50, 60, 70]
del listeu[2:6]
print(listeu)

# nomor 13
listeu = [10, 20, 30, 40, 50, 60, 70]
del listeu[:]
print(listeu)

# nomor 14
listeu = [10, 20, 30, 40, 50, 60, 70]
del listeu
print(listeu)

# nomor 15
listeu = [10, 20, 30, 40, 50, 60, 70]

print(5 in listeu)
print(10 in listeu)

# nomor 16
listeu = [10, 20, 30, 40, 50, 60, 70]

print(7  not in listeu)
print(50 not in listeu)

# nomor 17
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# nomor 18
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

# nomor 19
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemen ditemukan pada index ke-", i)
else:
    print("Tidak ada di dalam list")
# nomor 20
tebakan = [3, 7, 11, 42, 34, 49]

hasil_undian = [5, 9, 11, 42, 3, 49]

benar = 0

for angka in tebakan:
    if angka in hasil_undian:
        benar += 1

print("Jumlah tebakan yang benar:", benar)
# nomor 21
listeu =  [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

listbaru = []

for angka in listeu:
    if angka not in listbaru:
        listbaru.append(angka)

print("List setelah angka berulang dihilangkan:", listbaru)