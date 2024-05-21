def fact(num):
    # num=int(input("enter the number"))
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac
data=fact(4)
print(data)


def is_leapyear(year):
    if year%100==0 and year%400==0:
        return "leap year"
    elif year%100==0 and year%4==0:
        return "leap_year"
    else:
        return "not leap_year"
    
print(is_leapyear(2023))




  
  