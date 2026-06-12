def digit(n):
    stringdigit =  ""
    while (n > 0):
        x = n % 10 
        stringdigit = str(x) + stringdigit
        n = n// 10

    return stringdigit

n = int ( input ("enter number :"))
temp = n

q = digit( temp )

for i in q :
    print(i)


