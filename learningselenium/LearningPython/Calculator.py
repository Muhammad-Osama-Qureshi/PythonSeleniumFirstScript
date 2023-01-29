on=True


def add():
    x = float(input("Enter a Number"))
    y = float(input("Input Another Number"))
    print(x + y)


def sub():
    x = float(input("Enter a Number"))
    y = float(input("Input Another Number"))
    print(x - y)


def mul():
    x = float(input("Enter a Number"))
    y = float(input("Input Another Number"))
    print(x * y)


def div():
    x = float(input("Enter a Number"))
    y = float(input("Input Another Number"))
    print(x / y)

while on:
    typo = input("Type any operation from + - * / Q q")

    if typo == "+":
        add()
    elif typo == "-":
        sub()
    elif typo == "*":
        mul()
    elif typo == "/":
        div()
    elif typo == "q":
        on = False
    else:
        print("There is no operation like that sorry !")
