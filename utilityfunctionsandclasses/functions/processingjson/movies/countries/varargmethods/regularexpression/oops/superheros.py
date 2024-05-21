class SuperHeros:
    def __init__(self,name):
        self.name=name

    def super_powers(self):
        self.context=["run","jump"]
        return self.context
class SpiderMan(SuperHeros):

    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("fly")
        self.context.append("spread web")
        return self.context
    
class MinalMuraly(SuperHeros):
    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("speed")
        return self.context
    
os=SpiderMan("spiderman")
print(os.super_powers())


om=MinalMuraly("minalmuraly")
print(om.super_powers())