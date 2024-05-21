class Department:
    def __init__(self,name):
        self.name=name

    def super_sub(self):
        self.context=["AI","ML"]
        return self.context
    
class ComputerScience(Department):
    def super_sub(self):
        self.context=super().super_sub()
        self.context.append("COA")
        self.context.append("CD")
        return self.context
    
class Mechanical(Department):
    def super_sub(self):
        self.context=super().super_sub()
        self.context.append("Machine Design")
        return self.context
    
ocs=ComputerScience("computer science")
print(ocs.super_sub())


om=Mechanical("mechanical")
print(om.super_sub())