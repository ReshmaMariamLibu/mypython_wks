n1=int(input("enter num1"))
n2=int(input("enter num2"))
lst=[10,20,30]
loc=int(input("enter index position to fect object"))
# try:
#     res=n1/n2 
#     print(f"result={res}")

# except Exception as e:
try:
    print(lst[loc])
except Exception as e:
    print(e.args)
try:
    res=n1/n2
    print(f"result={res}")
except Exception as e:
    print(e.args)
    # print("exception occured")
print("database commit")
print("file transaction")