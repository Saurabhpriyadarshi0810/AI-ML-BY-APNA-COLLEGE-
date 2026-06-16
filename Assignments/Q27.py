word = input("enter word :")

count = 0 
for i in word :
    if i ==" ":
        count += 1 

print(f"Number of space in the word {word} is { count}")