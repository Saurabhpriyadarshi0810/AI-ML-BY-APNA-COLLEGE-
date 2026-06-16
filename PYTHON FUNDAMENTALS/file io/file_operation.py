# f = open("file path ", "mode")
# r --> read
# w --> write 

f = open("sample.txt" , "r")
# f is a file object
# data =f.read()

# print(type(data ))

data1 = f.readline()
print(data1)
data1 = f.readline()
print(data1)

f.close()