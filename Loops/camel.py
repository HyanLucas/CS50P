def main():
    camelCase = str(input("camelCase: "))
    snake_case_maker(camelCase)


def snake_case_maker(camelCase):
    snake_case = ""
    for letter in camelCase:
        if letter.isupper():
            if len(snake_case) > 0:
                snake_case += "_" + letter.lower()
        else:
            snake_case += letter
    return print(snake_case)


main()
