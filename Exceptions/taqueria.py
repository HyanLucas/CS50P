def main():
    total = 0.0
    while True:
        try:
            item = str(input("Item:")).title()
            total += item_value(item)
            print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            break


def item_value(item):
    item_menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    if item in item_menu:
        return item_menu[item]
    else:
        return 0


main()
