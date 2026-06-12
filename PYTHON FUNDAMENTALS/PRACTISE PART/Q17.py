while True :
    user_input = input("enter 'quit' to exit : ")

    if user_input == "quit":
        break 

    n = float(user_input)

    if n>0 :
        print("Positve")
    elif n < 0 :
        print("Negative")
    elif n == 0 :
        print("Zero")
