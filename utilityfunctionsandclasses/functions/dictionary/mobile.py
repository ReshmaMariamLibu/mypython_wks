mobile={"color":"red","brand":"Apple","price":99999}

print(mobile["brand"])

if "price" in mobile:
    print(mobile["price"])
else:
    print("invalid key")

mobile["offer"]=500
mobile["price"]-=500
print(mobile)