class Book:
    name:str
    author:str
    price:int
    publisher:str

    def __init__(self,name,author,price,publisher):
        #initializing attributes
        self.name=name
        self.author=author
        self.price=price
        self.publisher=publisher

    def display(self):
        print(self.name,self.author,self.price,self.publisher)

    def __str__(self):
        return self.name

book1=Book("Alice in wonderland","Lewis Carrol",1000,"john")
# book1.set_book("Alice in wonderland","Lewis Carrol",1000,"john")
# book1.display()
print(book1)


