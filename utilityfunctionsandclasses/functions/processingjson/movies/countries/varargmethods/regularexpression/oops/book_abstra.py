data=[
        {"id":100,"name":"Wings of Fire","price":700},
        {"id":101,"name":"Tom Sawyer","price":250},
        {"id":102,"name":"Harry Porter","price":800},
        {"id":103,"name":" War and Peace","price":500},
        {"id":104,"name":"Hamlet","price":900},
        

    ]


def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} created successfully"

def retrive(*args,**kwargs):
      id=kwargs.get("id")
      ob=[book for book in data if book.get("id")==id]
      return ob

print(create(id=102,name="Diary of a Wimpy Kid",price=350))
print(retrive(id=104))