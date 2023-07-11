def main():
    expression = str(input("Expression: "))
    math_interpreter(expression)


def math_interpreter(expression):
    x, y, z = expression.split(" ")
    match y:
        case "+":
            return print(f"{float(x) + float(z):.1f}")
        case "-":
            return print(f"{float(x) - float(z):.1f}")
        case "/":
            return print(f"{float(x) / float(z):.1f}")
        case "*":
            return print(f"{float(x) * float(z):.1f}")


main()
