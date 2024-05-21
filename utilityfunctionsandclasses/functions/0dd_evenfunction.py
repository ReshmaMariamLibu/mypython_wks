# def is_even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# print(is_even(6))


text="hello"
wc={}
for ch in text:
    if ch not in wc:
        wc[ch]=1
    else:
        wc[ch]+=1
        print(wc)
