import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    answer = str(input("Input: "))
    fonts = figlet.getFonts()
    figlet.setFont(font=random.choice(fonts))
    print("Output:", figlet.renderText(answer), sep="\n")
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":

        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit("Invalid usage")
        answer = str(input("Input: "))
        print("Output:", figlet.renderText(answer), sep="\n")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
