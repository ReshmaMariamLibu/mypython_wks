class Animal:
    name:str

    def __init__(self,name):
        self.name=name

    def sounds(self):
        pass

class Dog(Animal):
    def sounds(self):
        print(f"{self.name} barks")

    def __str__(self):
        return self.name

class Frog(Animal):
    def sounds(self):
        print(f"{self.name} croaks")

    def __str__(self):
        return self.name

objdog=Dog("dog")
objdog.sounds()
print(objdog) 
   
fobj=Frog("frog")
fobj.sounds()
print(fobj)   
     
print(objdog.__class__) #attribute no method reason
print(fobj.__class__)