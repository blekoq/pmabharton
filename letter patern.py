number=int(input("Mau di ulang berapa kali?"))
for x in range(97,number+97):
    print()
    for y in range(97,x):
     print(chr(y),end=" ")
for x in range(65,number+65):
    print()
    for y in range(65,x):
     print(chr(y),end=" ")