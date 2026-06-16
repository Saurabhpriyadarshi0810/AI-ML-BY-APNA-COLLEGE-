nums = [1,2,3,4,5,9,25,1,47,7,4,94464,54,1,465,4,648,89,65,456,4564,4,8]

seen = set()
duplicate = set()

for i in nums :
    if i in seen :
        duplicate.add(i)
    seen.add(i)

print(duplicate)    