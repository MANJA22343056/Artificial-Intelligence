while True:
    try:
        angka = int(input("Masukkan sebuah angka bulat: "))
        break  # keluar dari loop jika input berhasil dikonversi ke bilangan bulat
    except ValueError:
        print("Input yang Anda masukkan bukan bilangan bulat. Silakan coba lagi.")

if angka % 2 == 0:
    print("Angka tersebut adalah bilangan genap.")
else:
    print("Angka tersebut adalah bilangan ganjil.")
