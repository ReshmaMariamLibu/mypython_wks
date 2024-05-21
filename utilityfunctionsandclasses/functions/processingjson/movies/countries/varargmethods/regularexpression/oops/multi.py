class P1:
    def m1(self):
        print("inside parent1")

class P2:
    def m2(self):
        print("inside parent2")

class Child(P1,P2): # multiple inheritance
    def m3(self):
        print("inside child")

ch=Child()
ch.m1()
ch.m2()
ch.m3()