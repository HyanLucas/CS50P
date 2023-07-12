def main():
    phrase = str(input("Input: "))
    vowels_omitting(phrase)


def vowels_omitting(phrase):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        phrase = phrase.replace(vowel, "")
    return print("Output:", phrase)


main()
