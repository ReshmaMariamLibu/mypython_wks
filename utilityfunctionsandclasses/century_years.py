# print all century years from 1800 to 2024
year1=int(input("enter the lower number"))
year2=int(input("enter the  higher number"))
for n in range(year1,year2):
     if(n%100==0):
       print(n)

