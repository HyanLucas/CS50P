def main():
    greeting = str(input("Greeting: "))
    print(greeting_valor(greeting))


def greeting_valor(greeting):
    if greeting[:5].lower() == "hello":
        return "$0"
    elif greeting[0].lower() == 'h':
        return "$20"
    else:
        return "$100"


main()
