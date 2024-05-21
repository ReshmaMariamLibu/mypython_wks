#dictionary methods
#get("key")
#pop("key")
#item()
#key()
#value()

animals={"a":"apple","b":"banana","c":"cat","d":"dog","e":"elephant"}

#get{"key"}-to take value with key
print(animals.get("b"))
# print(animals.get("w")) ->  if not present  print none

#print all keys
#keys()

for k in animals.keys():
     print(k)

#values() -to print all values

for v in animals.values():
     print(v)

#item{} => return key,value
for k,v in animals.items():
    print(k,v)

#pop{key} -> to remove a key 
animals.pop("a")
print(animals)