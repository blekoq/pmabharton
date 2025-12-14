Akun={"alo2123":"###","blolbo222":"*#*","brelbrel":"0*54"}
while True:
    print("welcome to roblox pls login to continues")
    user=input("masukan username: ")
    pasw=input("masukan password: ")
    # print
    if user in Akun:
        print("akun di temukan")
        if pasw == Akun[user]:
            print("anda berhasil login")
        else:
            print("password salah")
    else:
        print("akun tidak terdaftar, mau register atau mau daftar? y/n: ")
        choice=input()
        if choice=="y" or choice=="Y":
            duser=input("masukan user name: ")
            dpasw=input("masukan password: ")
            Akun[duser]=dpasw
            print(Akun)
        else:
            print("PEGI KAU JAOG JAOH")
            break