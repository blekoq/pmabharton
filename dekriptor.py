pesan=input("masukan pesan yang akan di dekripsi: ")
code=int(input("masukan kode rahasia anda: "))
for i in pesan:
    print(chr(ord(i)-code), end="")
