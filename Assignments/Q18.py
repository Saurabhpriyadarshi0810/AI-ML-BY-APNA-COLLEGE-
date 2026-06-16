a = float(input ( "enter 1st number :"))
b = float(input ( "enter 2nd number :"))

symbol = input ("enter symbol to choose operator( '+' , '-' , '*' , '/') : ")

match symbol :
    case "+" :
        print(" sum = ",a+b)
    case "-" :
        print("  = difference",a-b)
    case "*" :
        print(" product = ",a*b)
    case "/" :
        print(" quotient  = ",a/b)
    case _ :
        print("invalid input !")