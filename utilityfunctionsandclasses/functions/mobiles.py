mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":1,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":65000},

    ]},
     {"id":1,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":45000},

    ]},
     {"id":1,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":35000},

    ]},


]

#35k below
# for mob in mobiles:
#     for v in mob.get("varients"):
for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price")<35000:
#           print(mob.get("name"))

all_mobile_names=[mob.get("name")for mob in mobiles ]
print(all_mobile_names)

#print all brands

# all_brands=[ mob.get("brand")for mob in mobiles]
# print(all_brands)

#print mobile names available in range of 20k to 40k


#20k to 30k
# for mob in mobiles:
#    for v in mob.get("varients"):
#       if v.get("price") in range(20000,30001):
#          print(mob.get("name"))



price_f=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]
print(price_f)

#ram filter
# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

ram_filter=[mob.get("name")for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]
print(ram_filter)

#costly
costly_price=max(v.get("price")for mob in mobiles for v in mob.get("varients"))
print(costly_price)
#8gb ram price <40000
ram_price=[mob.get("name")for mob in mobiles for v in mob.get("varients") if v.get("ram")=="8gb" and v.get("price") <=40000 ]
print(ram_price)