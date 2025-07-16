# input string, integer, float
string = input("Masukkan string: ")
integer = int(input("Masukkan bilangan bulat: "))
float = float(input("Masukkan bilangan desimal: "))

# gabungan string, integer, float menggunakan fungsi str()
hasilGabungan = string + " " + str(integer) + " " + str(float)

# cetak hasil 
print("Hasil penggabungan: ", hasilGabungan)
