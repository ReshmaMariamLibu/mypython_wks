# method overloading-> same class bt different no: of parameters
class Operations:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
op=Operations()
print(op.add(20,30,40,50))