a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

# operasi bitwise
bitwiseAND = a & b
bitwiseOR = a | b
bitwiseXOR = a ^ b
bitwiseNOTA = ~a
bitwiseNOTB = ~b

# menampilkan hasil operasi bitwise beserta representasi binernya
print("Hasil operasi bitwise AND:", bitwiseAND, "(", bin(bitwiseAND), ")")
print("Hasil operasi bitwise OR:", bitwiseOR, "(", bin(bitwiseOR), ")")
print("Hasil operasi bitwise XOR:", bitwiseXOR, "(", bin(bitwiseXOR), ")")
print("Hasil operasi bitwise NOT bilangan pertama:", bitwiseNOTA, "(", bin(bitwiseNOTA), ")")
print("Hasil operasi bitwise NOT bilangan kedua:", bitwiseNOTB, "(", bin(bitwiseNOTB), ")")
