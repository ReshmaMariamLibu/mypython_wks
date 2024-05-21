low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

for num in range(low,upp+1):
    if(num%2!=0):
       print(num)