def is_prime( n ):
    x = True
    for i in range (2 , n-1 ):
        if n % i == 0:
            x = False
    return x 

n =  int ( input ("enter the number :"))
x = is_prime(n)

if x != True :
    print(n," is prime")
else:
    print(n," is  not prime")
