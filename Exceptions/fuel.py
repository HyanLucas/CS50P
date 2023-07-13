def main():
    gauge_calculate()


def gauge_calculate():
    values = []
    while True:
        gauge = str(input("Fraction: "))
        try:
            value1, value2 = gauge.split("/")
            value1, value2 = int(value1), int(value2)
        except ValueError:
            pass
        if value1 > value2:
            pass
        else:
            break
    if value2 != 0:
        if value1 != 0:
            result = float(value1 / value2)
            if value1 == value2:
                return print("F")
            elif result == 0.25:
                return print("25%")
            elif result == 0.50:
                return print("50%")
            elif result == 0.75:
                return print("75%")
        else:
            return print("E")


main()
