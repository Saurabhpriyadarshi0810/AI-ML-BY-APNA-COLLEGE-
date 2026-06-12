marks = [100,99,62,56,48,]

print(marks)
print(len(marks))
print(marks[:4])
print(marks[:4:2])

marks.append(25)
marks.insert(4,26)
marks.sort()
marks.sort(reverse=True)

marks.reverse()
print(marks)

#loops in list 

nums = [2 ,5,7,8,9,11]

indx = 0
x = 8
for i in nums :
    if x == i:
        print(f"{x} found at the index {indx}")
        break  
    else:
        indx += 1    