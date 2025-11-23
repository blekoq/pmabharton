import random 
solsRNG=["1/5 skorpion","1/30 BLEKOQ","1/100000000000 SCAVENGER"]
while(True):
    getc=(random.randint(1,100000000100 ))
    if(getc<= 20000000000):
        print(solsRNG[0])
    elif(getc<= 30000000000):
        print(solsRNG[1])
    elif(getc>= 99999999999):
        print(solsRNG[2])
        break
    else:
        print(solsRNG[0])