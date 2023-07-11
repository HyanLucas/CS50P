def main():
    result = str(input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    print(answer(result))


def answer(result):
    if result == "42" or result == "forty-two" or result == "Forty Two":
        return "Yes"
    else:
        return "No"


main()
