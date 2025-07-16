a = float(input("Masukkan panjang sisi A: "))
b = float(input("Masukkan panjang sisi B: "))
c = float(input("Masukkan panjang sisi C: "))

if a == b == c:
    print("Segitiga tersebut adalah segitiga sama sisi.")
elif a == b or a == c or b == c:
    print("Segitiga tersebut adalah segitiga sama kaki.")
else:
    print("Segitiga tersebut adalah segitiga sembarang.")
