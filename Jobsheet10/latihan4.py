n = int(input("masukkan jumlah suku fibonacci yang inin ditampilkan: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("masukkan bilangan bulat positif")
elif n == 1:
    print("deret fibonacci hingga suku ke-", n, ":", a)
else:
    print("deret fibnacci hingga suku ke-", n, ":")
    while count < n:
        print(a, end = " ")
        nth = a + b
        a = b 
        b = nth
        count += 1