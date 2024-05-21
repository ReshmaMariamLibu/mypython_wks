# Inheritance ->(single inheritance,multiple inheritance,multilevel inheritance)
class P1:
    def m1(self):
        print("inside parent1")

class P2(P1):
    def m1(self):
        print("inside parent2")

class Child(P2): # multiple inheritance
    def m3(self):
        print("inside child")

ch=Child()
ch.m1()
