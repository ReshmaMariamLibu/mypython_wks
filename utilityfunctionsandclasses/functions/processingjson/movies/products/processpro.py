from json import load
path="C:\\Users\\user\\Desktop\\my_pythonworks\\utilityfunctionsandclasses\\functions\\processingjson\\movies\\products\\items.json"
with open(path,encoding="utf-8") as f:
    data=load(f)
#print total no: of products
# print(len(data)) 

#q1 print all categories
all_categories={p.get("category") for p in data}
#print(all_categories)

#q2 print electronics product name
electronic_items=[p.get("title")for p in data if p.get("category")=="electronics"]
# print(electronic_items)

#q3 top rated product
top_ratedproduct=max(data,key=lambda p:float(p.get("rating").get("rate")))
# print(top_ratedproduct.get("title"))

#q4 product having category women's clothing price range (100-300)

# for p in data:
    # if p.get("category")=="women's clothing" and p.get("price")>20 and p.get("price")<=30:
    #  print(p.get("title"))

#q5 which product got most number of ratings

most_reviewed_product=max(data,key=lambda p:p.get("rating").get("count"))
# print(most_reviewed_product.get("title"))

#q6 jewellery product with rating >3


#q7 sort product wrt price order by dec
srt_product=sorted(data, reverse=True,key=lambda p:p.get("price"))
for p in srt_product:
#  print(p.get("title"))

 #q8 categorywise product count

 wc={}
 for p in data:
   category=p.get("category")
   if category not in wc:
      wc[category]=1
   else:
    wc[category]+=1
# print(wc)

val_key=[(v,k)for k,v in wc.items()]
# print(max(val_key))
# print(sorted(val_key))
# print(min(val_key))
print(val_key)
print(min(val_key,key=lambda lst:lst[0]))

orders={}
