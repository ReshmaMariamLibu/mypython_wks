

for leap in range(1999,2005):
    
    if (leap%100==0) and (leap%400==0):
        print(leap)
    elif(leap%100!=0) and (leap%4==0):
        print(leap)    