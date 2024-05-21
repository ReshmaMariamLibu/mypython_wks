weightin_kg=78
heightin_cm=165
height_m=heightin_cm/100
bmi=weightin_kg/(height_m**2)
print(bmi)  
if(bmi<20):
    print("is under weight")
elif(bmi>=20 and bmi<25):
   print("is normal")
elif(bmi>=25 and bmi<30):
    print("over weight")
elif(bmi>=30):
    print(" obesity")
