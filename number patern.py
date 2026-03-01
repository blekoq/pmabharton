number=int(input("Mau di ulang berapa kali?"))
for x in range(number):
    print()
    for y in range(x+1):
        print(y+1,end=" ")
        
for x in range(number):
    print()
    for y in range(x+1):
        print(x+1,end=" ")   

for x in range(number):
    print()
    for y in range(1,x*2,2):
        print(y,end=" ")