for _ in range(5):
    try:
        x = int(input("Choose x (1, 2, 3, 4, 5)= "))
        if x == 1:
            print("Your choise is 1")
        elif x == 2:
            print("Your choise is 2")
        elif x == 3:
            print("Your choise is 3")
        elif x == 4:
            print("Your choise is 4")
        elif x == 5:
            print("Your choise is 5.")
        else:
            print("Unknown choise!")
    except ValueError:
            print("Invalid Input")