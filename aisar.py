pesan=input("masukan pesan rahasia anda: ")
code=int(input("masukan kode rahasia anda: "))
for i in pesan:
    print(chr(ord(i)+code), end="")
