from emoji import emojize


def main():
    answer = str(input("Input: "))
    transform(answer)


def transform(answer):
    return print(emojize("Output: " + answer))


main()
