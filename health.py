gender="male"
tummy_size=80
buttock_size=75
value=tummy_size/buttock_size
if(gender=="male"):
   if(value<0.95):
    print("low")
   elif(value>=0.96 and value<1.0):
    print("moderate")  
   else:
    print("high")
elif(gender=="female"):
   if(value<0.80):
       print("low")
   elif(value >=0.80 and value <0.85):
    print("moderate")
   else:
    print("high")