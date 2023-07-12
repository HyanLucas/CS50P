def main():
    meal_time = str(input("What time is it? "))
    convert(meal_time)


def convert(time):
    hour = time.split(":")[0]
    challenge = time.split(" ")[1]
    match hour:
        case "7":
            if challenge == "a.m.":
                return print("breakfast time")
        case "07":
            if challenge == "a.m.":
                return print("breakfast time")
        case "12":
            if challenge == "a.m.":
                return print("lunch time")
        case "6":
            if challenge == "p.m.":
                return print("dinner time")
        case "06":
            if challenge == "p.m.":
                return print("dinner time")


if __name__ == "__main__":
    main()
