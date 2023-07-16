def main():
    print("Amount Due: 50")
    coin()


def coin():
    coke_value = int(50)
    while True:
        coin_value = int(input("Insert Coin: "))
        if coin_value == 25 or coin_value == 10 or coin_value == 5:
            if coke_value >= coin_value:
                coke_value -= coin_value
        if coke_value > 0:
            print(f"Amount Due: {coke_value}")
        else:
            print(f"Change Owed: {coke_value * (-1)}")
            break


main()
