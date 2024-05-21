min_two=lambda n1,n2:n1 if n1<n2 else n2
max_num=lambda n1,n2:n1 if n1>n2 else n2
odd_even=lambda n:"even" if n%2==0 else "odd"
num_chck=lambda n:"+ve" if n>0 else "-ve"
print(num_chck(4))
print(min_two(10,7))
print(odd_even(8))
print(max_num(20,30))

      