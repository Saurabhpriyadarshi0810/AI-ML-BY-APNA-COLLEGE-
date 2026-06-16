f = open("sample.txt","w")

f.write("text to be overwritten \nby the write operation\n")

f= open("sample.txt","r")
data = f.read()
print(data)
f.close