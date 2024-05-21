num1=int(input("enter the number"))
num2=int(input("enter the number"))
hcf=1
sm_num=num1 if num1<num2 else num2
for i in range(1,sm_num+1):
    if(num1%i==0)and (num2%i==0):
       hcf=i
       print(hcf)