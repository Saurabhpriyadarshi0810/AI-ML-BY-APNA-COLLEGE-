def sum_of_digit(n):
    sum = 0
    while (n > 0):
        x = n % 10 
        sum += int(x)
        n = n// 10

    return sum

n = int ( input ("enter number :"))
temp = n

q = sum_of_digit( temp )

print( "sum of digits of ",n ," is :",q)