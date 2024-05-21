num1=10
num2=100
num3=70
if((num1>num2) and (num1>num3)):
    print("num1 is largest")
    if(num2>num3):
        print(f" {num2} is second largest number")
    else:
        print("num3 is second largest")
elif((num2>num1) and (num2>num3)):
    print("num2 is largest")
    if(num1>num3):
        print(f"{num1} is second largest number")
    else:
        print(f"{num3} is second largest number")
elif((num3>num1) and (num3>num2)):
    print("num3 is largest")
    if(num1>num2):
        print(f"{num1} is second largest numnber")
    else:
        print(f"{num2} is second largest number")