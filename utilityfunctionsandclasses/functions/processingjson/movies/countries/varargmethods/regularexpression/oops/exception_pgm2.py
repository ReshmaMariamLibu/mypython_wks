n1=int(input("enter num1"))
n2=int(input("enter num2"))

try:
    res=n1/n2
    print(f"result={res}")
except Exception as e:
    n2=int(input("enter value for n2"))
    res=n1/n2
    print(f"result={res}")
finally:
    print("database commit")
    print("file transaction")
