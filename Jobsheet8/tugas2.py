bilangan = int(input("Masukkan sebuah bilangan bulat: "))

# inisialisasi variabel untuk menyimpan jumlah bit 1
jumlahBit1 = 0

while bilangan:
    jumlahBit1 += bilangan & 1
    bilangan >>= 1

print("Jumlah bit 1 (bit set) dari bilangan tersebut adalah:", jumlahBit1)