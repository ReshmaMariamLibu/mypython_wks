num=int(input("enter the number"))

is_prime=True
for n in range(2,num):
   if(num%n==0):
    is_prime=False
    break
print(is_prime)

