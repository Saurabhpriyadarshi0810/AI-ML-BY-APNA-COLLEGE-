dict = {}
print( " A - Add a student \nB - update marks \nC - Search  For a student \nD - Display all Students and marks ")
choice = input("enter  options :")

match choice :
    case "A": dict.update({input("enter key :"):int( input("enter value"))})
    case "B" :dict[input("enter  key whose marks you want to update :")] = int(input("enter marks  :"))
    case "C" : print(dict.get(input("enter  key to search :")))
    case "D" : print(dict)
    case _ : print("invalid choice !")