# fungsi untuk memasak gyukaku
# fungsi untuk menyiapkan bahan
def  siapkanbahan():
    print("pilih daging (1 s/d 5)")
    print("1.karubig")
    print("2.rosuw")
    print("3.HARAM")
    print("4.ciken")
    print("5.siput") 
    daging=input()
    if(daging=="1"):
        print("kamu memilih karubiq")
    elif(daging=="2"):
        print("kamu memilih rosuw")
    elif(daging==3):
        print("kamu memilih HARAM")
    elif(daging=="4"):
        print("kamu memilih ciken")
    elif(daging=="5"):
        print("kamu memilih siput")
    else:
        print("pergi loe syuh syuh")
    print("pilih saos")
    print("1.kecap")
    print("2.garlik sious")
    print("3.misou sious")
    print("4.spaisi umakhara")
    saos=input()
    if(saos=="1"):
        print("kamu memilih kecap")
    elif(saos=="2"):
        print("kamu memilih garlik sious")
    elif(saos=="3"):
        print("kamu memilih misou sious")
    elif(saos=="4"):
        print("kamu memilih spaisi umakhara")
    else:
        print("pergi loe syuh syuh")
def memasak(porsi):
    print("memasak gyukaku ", porsi, "porsi")
def takeaway():
    print("makan di tempat atau takeaway?")
siapkanbahan()
porsi=input("masukan jumlah porsi yang ingin di masak: ")
memasak(porsi)

    
    