def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) <= 6 and len(plate) > 2:
        if plate[0].isalpha() and plate[1].isalpha():
            cont_number = 0
            zero_first = False
            letter_after_number = False
            for number in plate:
                if number == "0" and cont_number == 0:
                    zero_first = True
                if number.isdigit():
                    cont_number += 1
                if number.isalpha() and cont_number > 0:
                    letter_after_number = True
            if zero_first or letter_after_number:
                return False
            elif "." in plate or "," in plate or " " in plate or "'" in plate:
                return False
            else:
                return True
        else:
            return False
    else:
        return False


main()
