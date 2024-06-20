ans = ""
while ans != "n":
    try:
        num = int(input("Enter num = "))
        if num == 0 :
            print("Zero")
        elif num == 1:
            print("One")
        elif num == 2:
            print("Two")
        elif num == 3:
            print("Three")
        elif num == 4:
            print("Four")
        elif num == 5:
            print("Five")
        elif num == 6:
            print("Six")
        elif num == 7:
            print("Seven")
        elif num == 8:
            print("Eight")
        elif num == 9:
            print("Nine")
        elif num == 0:
            print("Zero")
        else:
            print("Unknow input!")
        ans = input("Continue y/n ")
    except ValueError:
        print("Invalid input.")
    

