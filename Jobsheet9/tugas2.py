totalBelanja = float(input("Masukkan total belanja: "))

if totalBelanja > 100000:
    diskon = 0.1 * totalBelanja
else:
    diskon = 0

totalPembayaran = totalBelanja - diskon

print("Total pembayaran setelah diskon adalah:", totalPembayaran)
