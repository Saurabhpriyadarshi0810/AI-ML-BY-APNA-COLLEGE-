data = True
word = "store"
line = 1

with open("sample4.txt" , "r") as f :
    while data :
        data = f.readline()

        if word in data:
            print(f"{word} found at line {line}")
            break
        
        line += 1