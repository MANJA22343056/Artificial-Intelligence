while True:
    try:
        angka = int(input("Masukkan sebuah angka: "))
        if angka % 2 == 0:
            print("Angka tersebut adalah bilangan genap.")
        else:
            print("Angka tersebut adalah bilangan ganjil.")
        break
    except ValueError:
        print("Input bukan angka. Silakan coba lagi.")
