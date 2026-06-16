# it is similar to switch case 
print("enter color in small letter only !")
color = input ( "enter color : ")

match color :
    case"green":
        print("Go")
    case"red":
        print("Stop")
    case"yellow":
        print("look")
    case _ :
        print("invalid color !")