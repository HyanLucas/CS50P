from random import randint


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                pass
            else:
                break
        except ValueError:
            pass
    random_number = generate_random_number(level)
    guess = 0
    while random_number != guess:
        try:
            guess = int(input("Guess: "))
            if guess > random_number:
                print("Too large!")
            elif guess < 1:
                pass
            elif guess < random_number:
                print("Too small!")
            else:
                print("Just right!")
        except ValueError:
            pass


def generate_random_number(value):
    return randint(1, value)


main()
