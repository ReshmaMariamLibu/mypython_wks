#inheritance

class Parent:

    def mobile(self):
        print("samsung a52s")

    def bike(self):
        print("passionpro")

class Child(Parent):
    pass

obj=Child()
obj.mobile()
obj.bike()