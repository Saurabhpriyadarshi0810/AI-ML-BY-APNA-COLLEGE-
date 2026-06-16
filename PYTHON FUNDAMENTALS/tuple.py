tup = (1,2,3,4,5,6,"abc",3.1456)
print(tup)
print(type(tup))

x = (1) # expression 
print(type(x))
x = (1,) # tupple 
print(type(x))

tup = (1,2,3,4,5)

sum = 0
for val in tup:
    sum += val 

print(f"sum of the values of the tupple {tup} is {sum}")

seq =  (1,2,3,4,5,4,3,2,2,2,1)
print(seq.index(2))
print(seq.count(2))

#count is used to  count no of occurance while index is used to find the index of first element occured 