print("welcome to BMI calculator")
berat=int(input("berapa berat badan mu?(kg): "))
tinggi=int(input("berapa tinggi badan mu?(cm): "))
tinggim=tinggi/100
BMI=berat/tinggim**2 
print(BMI)
# gemuk
if(BMI>25):
    print("kamu gemuk silahkan [DIET]")
elif(BMI<25 and BMI>18.5) :
    print("beratmu okepas pertahankan ")
else:
    print("beratmu kurang silahkan makan lebih banyak")

