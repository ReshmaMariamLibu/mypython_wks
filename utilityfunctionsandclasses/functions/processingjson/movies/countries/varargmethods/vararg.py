
def product(*args): #*accepts any num of parameters in tuple format
   res=1
   for n in args:
     res=res*n
   return res

print(product(10,20))
print(product(1,2,3,4,5))

def adder(*args):
 return sum(args)
print(adder(10,20))
print(adder(10,20,30))

def concat_strings(*args):
#     res=""
#     for st in args:
#      res+=st
#     return res

# print(concat_strings("hello","good","morning","all"))
  return "#".join(args)
print(concat_strings("hello","hai","hello")) 

def reverse_concat(*args):
  data=list(args)
  data.reverse()
  return " ".join(data)
print(reverse_concat("red","green","blue"))

def person_name(**kwargs):# ** accepts any no: of parameters in dictinory format
  print(kwargs)
person_name(first_name="sachin",middle_name="ramesh",last_name="tendulkar")

def empdetails(**kwargs):
  print(kwargs)
  name=kwargs.get("name")
  exp=kwargs.get("exp")
  dep=kwargs.get("dep")
  print(f"{name} has {exp} year exp in {dep}" )
empdetails(name="john",exp="2",dep="web development")

def balance_enq(**kwargs):
  print(kwargs)
  bank_name=kwargs.get("bank_name")
  acno=kwargs.get("acno")
  balance=kwargs.get("balance")
  print(f"your {bank_name} {acno} account bal is INR {balance} ")

  #your sbi 12334 account bal is INR 23455
balance_enq(bank_name="sbi",acno="12334",balance=23455 )

def perform_operation(*args,**kwargs):
  num1,num2=args
  op=kwargs.get("operand")
  if op=="+":
    return num1+num2
  elif op=="-":
    return num1-num2
  elif op=="*":
    return num1*num2
  else:
    return "invalid operand"
print(perform_operation(10,20,operand="*"))
  


