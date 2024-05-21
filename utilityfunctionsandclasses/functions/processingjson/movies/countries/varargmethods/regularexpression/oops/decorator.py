#decorator : simply a normal fn
#rule1: function contains another fn
#rule2:it contains an inner fn
#rule3:no: of parameters is the no of parameters inside the fn that we want to decorate

def swap_num(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@swap_num
def sub(n1,n2):
    return n1-n2

@swap_num
def div(n1,n2):
    return n1/n2

print(sub(2,10))
print(div(2,8))