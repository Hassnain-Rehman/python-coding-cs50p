from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")