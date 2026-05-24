untukbuahbuahan=["apple","jeruk","buah naga","semangka"]#list
hargabuah=[70000,80000,300000,100000]
# print(untukbuahbuahan)
# print(untukbuahbuahan[1:3])
untukhewan=("walang","walang sanget","lembeng","curut")#tuple  
# print(untukhewan[1:3])
untukbuahbuahan[0]="buah apel"
# print(untukbuahbuahan)
# untukhewan[0]="belalang"
# print(untukhewan)
untukbuahbuahan.append("buah belimbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeng")
# print(untukbuahbuahan)
# untukhewan.append("aing maungggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggsggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggoggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggsgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
# print(untukhewan)
untuksayur={"kol":7000000,"kubeis":800000,"beton":3000000,"sambel":700000}#dictionary
# print(untuksayur)
untuksayur["kol"]=10000000
# print(untuksayur)
untuksayur["sambel bledek khas kali ciliwung"]=10000000
# print(untuksayur)
print("welcome to pasar mundur makmur sayur dan buah")
print("daftar sayur yang tersedia:")
angka=1
for sayur in untuksayur:
    print(angka, ".", sayur, ": Rp", untuksayur[sayur])
    angka+=1
totalbelanja=0
daftarbelanja={}
# print (list(untuksayur.values())[3-1])
while True:
    print("masukan angka sayur yang ingin di beli:")
    pilihan=int(input())
    jumlah=int(input("berapa kilo :"))
    daftarbelanja[pilihan]=jumlah
    selesai=input("apakah sudah selesai belanja? (y/n)")
    if selesai.lower() == "y":
        break
print()
print("daftar belanjaan anda:")
for belanjaan in daftarbelanja:
    print((list(untuksayur.keys())[belanjaan-1]), ":", daftarbelanja[belanjaan], "kilo")
for belanjaan in daftarbelanja:
    totalbelanja+=(list(untuksayur.values())[belanjaan-1])*daftarbelanja[belanjaan]
print()   
print("total belanjaan anda adalah: Rp", totalbelanja)
