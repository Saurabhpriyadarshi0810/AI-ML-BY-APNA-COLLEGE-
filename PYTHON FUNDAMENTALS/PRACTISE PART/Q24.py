tup = (1,3,2,4,5,6,7,8,9)

even_tup = ()
odd_tup = ()
for i in tup :
    if i % 2 == 0:
        even_tup+= (i,)
    else :
        odd_tup += (i,)

print(even_tup)
print(odd_tup)