from collections import defaultdict

grocery_list = defaultdict(int)
while True:
    try:
        item = input().upper()
    except EOFError:
        break
    grocery_list[item] += 1

for item_list in sorted(grocery_list):
    print(grocery_list[item_list], item_list)
