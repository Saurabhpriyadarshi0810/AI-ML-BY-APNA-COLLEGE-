list1 = [1,23,4,5,8,2]

list2 = [1,123,4,51,18,12]

set1 = set(list1)

set2 = set(list2)

seq = set1.intersection(set2)
a = list(seq)
x = len(a)

if x== 0 :
    print(f"no common elements")
else:    
    print(f"{seq}  are common elements")