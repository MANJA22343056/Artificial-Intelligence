tahun = int(input("Masukkan tahun: "))

kabisat = (tahun % 4 == 0) and (tahun % 100 != 0 or tahun % 400 == 0)

if kabisat:
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")
