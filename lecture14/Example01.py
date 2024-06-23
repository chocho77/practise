from pkg.hello import HelloClass

def print_hi(name):
    print(f'Hi, {name}.')

def hello_user()-> str:
    return "Hello, user."

def hello_user_again()-> str:
    return "Hello, user again."



if __name__ == '__main__':
    hello_class = HelloClass()
    hello_class.print_hi("Chavdar")
    print("Hi, main")

    hello = hello_user()
    hello_again = hello_user_again()


    print(hello)
    print(hello_again)
    print_hi("Chavdar")
    print_hi("Todor")
    print_hi("Yordan")
    print_hi("chocho")


