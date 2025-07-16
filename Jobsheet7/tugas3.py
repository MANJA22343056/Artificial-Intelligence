kata = input("Masukkan sebuah kata atau frase: ")

# Menghilangkan spasi dan mengubah semua huruf menjadi huruf kecil
kata = kata.replace(" ", "").lower()

palindrome = kata == kata[::-1]

if palindrome:
    print("Kata atau frase tersebut adalah palindrom.")
else:
    print("Kata atau frase tersebut bukan palindrom.")
