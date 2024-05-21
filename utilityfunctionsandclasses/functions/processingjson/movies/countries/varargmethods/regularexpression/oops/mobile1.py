data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]


def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} created successfully"

def retrieve(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id]
    return obj

#list all resources
def get(*args,**kwargs):
    return data

#delete
def destroy(*args,**kwargs):
    id=kwargs.get("id")
    obj=[ mob for mob in data if mob.get("id")==id].pop() #[0]
    data.remove(obj)
    return f"{obj} removed from db"

#update
def put(id,*args,**kwargs):
    obj=[mob for mob in data if mob.get("id")==id].pop()
    obj.update(kwargs)
    return f"{obj} has been updated"

# print(get())

# print(create(id="101",name="iphone12",price=78000))

# print(retrieve(id=100))

# print(destroy(id=100))
print(put(id=100,name="samsunggalaxya50",price=45000))

