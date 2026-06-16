word = "python"
print(word[3])

for i in word :
    print(i)

# word[1] = 'h' this is not possible in python as string is immutable 

print(word[-5:-1])

# String formating 

#1st method  normal method ( which uses format function } 

a = 10 
b = 5 
sum = a+b 
print("Sum of {} and {} is {}".format(a,b,sum))

# index based formating 
print("Sum of {1} and {0} is {2}".format(a,b,sum))

#2nd method ( used f string method )

a = 11 
b = 59
sum = a+b 
print(f"sum of {a} and {b} is {sum}")
print(f"average of {a} and {b} is {sum/2}")