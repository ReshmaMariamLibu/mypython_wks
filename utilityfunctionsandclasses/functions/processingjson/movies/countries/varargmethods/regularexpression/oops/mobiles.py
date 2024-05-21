class Mobiles:

   data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]
   
   #create method for
   def create(self,*args,**kwargs):
      self.data.append(kwargs)
      return f"{kwargs} created!!!!"
   
   #retreive
   def retrieve(self,id,*args,**kwargs):
      obj=[mob for mob in self.data if mob.get("id")==id].pop()
      return obj
   
   #list resources
   def get(self,*args,**kwargs):
      return f"{self.data}"
   
   #update
   def put(self,id,*args,**kwargs):
      obj=[mob for mob in self.data if mob.get("id")==id].pop()
      obj.update(kwargs)
      return f"{obj} updated!!!!"
   
   #delete
   def destroy(self,id,*args,**kwargs):
      obj=[ mob for mob in self.data if mob.get("id")==id].pop()
      self.data.remove(obj)
      return f"{obj} removed!!!!"
      
obj=Mobiles()
# print(obj.create(id="105",name="iphone12",price=70000))
# print(obj.retrieve(102))
print(obj.get())
print(obj.put(id=104,name="oneplus nord",price=50000))
print(obj.destroy(103))