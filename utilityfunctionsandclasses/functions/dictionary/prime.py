num=int(input("enter the number"))
prime=[ num%i==0 for i in range(2,num-1)]
print("prime"if any(prime)==False else "not prime")