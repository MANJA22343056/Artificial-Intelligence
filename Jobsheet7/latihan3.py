status = input("apakah anda memiliki akses? (ya/tidak): ").lower()

if status == "ya":
    print("anda memiliki akases penuh")
elif status == "tidak":
    print("anda tidak memiliki akses")
else:
    print("masukkan jawaban yang valid")