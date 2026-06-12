def hello(): # function definition
    print("hello world !")

hello() # function call 


def sum( a , b ):
    s = a +b 
    return s 

print("sum = ",sum(24,25))



def avg( a , b  ,c=0): # here c is default variable 
    s = a +b+c
    return s/3

print("sum = ",avg(24,25,2))
print("sum = ",avg(24,25))