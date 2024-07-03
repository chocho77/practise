def user_input():
    try:
        user_input = int(input("Enter int number: "))
        if isinstance(user_input, int):
            print(type(user_input))
    except ValueError:
        print("Wrong input.")

if __name__ == '__main__':
    user_input()



