#method overriding -> relationship,method signature must be same

class Parent:

    def mobile(self):
        print("samsung galaxy a53s")

    def car(self):
        print("KIA")

class Child(Parent):
    def mobile(self):
        print("iphone 15")

ch=Child()
ch.mobile()
ch.car()
