val=input(("enter the number"))
# if val.isdigit()==False:
#     raise Exception("only integers allowed")
# else:
#    print("test pass")

if val.isalnum()==False:
    raise Exception(" only alphanumeric allowed")
else:
    print("test pass")
