a = int(input("Masukkan nilai variabel pertama (a): "))
b = int(input("Masukkan nilai variabel kedua (b): "))

# tukar nilai variabel tanpa menggunakan variabel tambahan
a = a + b
b = a - b
a = a - b

# tampilkan nilai variabel yang telah ditukar
print("Setelah pertukaran:")
print("Nilai variabel pertama (a):", a)
print("Nilai variabel kedua (b):", b)
