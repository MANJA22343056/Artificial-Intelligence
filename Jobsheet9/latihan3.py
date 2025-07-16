beratBadan = float(input("masukkan berat badan (kg): "))
tinggiBadan = float(input("masukkan tinggi badan (m): "))

imt = beratBadan / (tinggiBadan ** 2)

if imt < 18.5:
    print("anda termasuk dalam kategori kurus")
elif imt >= 18.5 and imt < 25:
    print("anda termasuk dalam katagori normal")
else:
    print("anda termasuk dalam katagori gemuk")