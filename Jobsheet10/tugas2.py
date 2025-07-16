bilangan = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))

faktorial = 1

for i in range(1, bilangan + 1):
    faktorial *= i

print("Faktorial dari", bilangan, "adalah:", faktorial)