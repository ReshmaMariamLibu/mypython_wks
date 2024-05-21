#duplication not allowed,insertion order is not preserved,set(),indexing not supported
#methods-add(),union(),intersection(),pop(),remove(),discard()

# st={"one",2,"three",3.0,4,4}
# print(st)

# color_st={"red","green","blue"}

# color_st.add("yellow")

# print(color_st)

st1={"red","blue","yellow","orange"}
st2={"red","green","purple","orange","yellow","blue"}
# union_set=st1.union(st2)
# print(union_set)

# diff_set=st1.difference(st2)
# print(diff_set)

#to remove a specified object from a set
# st1.remove("red")
# print(st1)

# st1.discard("white")
# print(st1)

print(st1.issubset(st2))
print(st2.issuperset(st1))

# intersection_set=st1.intersection(st2)
# print(intersection_set)

# lst1=[11,12,13,14,15]
# lst2=[10,12,16,13,14]
#  #to print common elements from 2 list
# st_lst1=set(lst1)
# st_lst2=set(lst2)
# common_elements=st_lst1.intersection(st_lst2)
# print(common_elements)