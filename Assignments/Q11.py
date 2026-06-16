salary = int ( input ("enter salary: "))
if ( salary < 30000):
    print("tax rate is 5% ")
    print ( (salary *5)/100 )
elif ( salary >= 30000 and salary <= 70000):
    print("tax rate is 15% ")
    print ( (salary *15)/100 )
if ( salary > 70000):
    print("tax rate is 25% ")
    print ( (salary * 25)/100 )