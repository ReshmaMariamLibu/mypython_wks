# super -> refers  to parent class
class Parent:

    def vehicles(self):
        self.context=["passionpro","swift"]
        return self.context
    
class Child(Parent):
    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("ola")
        return self.context
    
p=Parent()
print(p.vehicles())

c=Child()
print(c.vehicles())
