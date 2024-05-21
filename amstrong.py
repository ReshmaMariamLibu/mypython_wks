num=input("enter the number")
digit_count=len(num)
num=int(num)
original=num

sum=0
while(num!=0):
   last_digit=num %10
   power=last_digit**digit_count
   sum=sum+power
   num=num//10
if original==sum:
    print("amstrong number")
else:
     print("not amstrong number")