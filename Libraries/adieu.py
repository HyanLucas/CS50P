import inflect

names = []
ift = inflect.engine()
while True:
    try:
        answer = input("Name: ")
        names.append(answer)
    except EOFError:
        if len(names) > 1:
            last_name = names[-1]
            names = ", ".join(names[0:-1])
            print("Adieu, adieu, to", names, "and", last_name)
            break
        if len(names) == 1:
            print("Adieu, adieu, to", names[0])
            break
