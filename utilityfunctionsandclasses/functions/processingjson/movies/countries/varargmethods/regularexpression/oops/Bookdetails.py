class Books:
  data=[
        {"id":100,"name":"python","price":350},
        {"id":101,"name":"java","price":450},
        {"id":102,"name":"django Porter","price":800},
        {"id":103,"name":" html","price":1300},
        {"id":104,"name":"bootstack","price":900},
        
    ]
  
  def create(self,*args,**kwargs):
    self.data.append(kwargs)
    return f"{kwargs} created!!!!!"
  
  def retreive(self,*args,id,**kwargs):
    obj=[b for b in self.data if b.get("id")==id].pop()
    return obj
  
  def get(self,*args,**kwargs):
    return f"{self.data}"
  
  def put(self,id,*args,**kwargs):
    obj=[b for b in self.data if b.get("id")==id].pop()
    obj.update(kwargs)
    return f"{obj} has been updated!!!!"
  
  def destroy(self,id,*args,**kwargs):
    obj=[b for b in self.data if b.get("id")==id].pop()
    self.data.remove(obj)
    return f"{obj} has been deleted!!!!!"
  

obj=Books()
print(obj.create(id=104,name="bootstrack",price=900))
print(obj.retreive(id=103))
print(obj.get())
print(obj.put(id=102,name="django",price=800))
print(obj.destroy(id=104))

