#defining a function
#add
#product
#divi
#cube
#sub
#factorial
#leap_year
#odd_even
def add(n1,n2):
     return n1+n2 
print(add(100,200))#100 and 200 are arguments

def prod(n1,n2):
    return n1*n2

def divi(n1,n2):
    return n1/n2

def cub(n):
    return n**3

def sub(n1,n2):
    return n1-n2
print(sub(10,5))

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
print(smart_sub(5,10))
