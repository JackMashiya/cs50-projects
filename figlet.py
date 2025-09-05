import sys
import random
import pyfiglet

def main():
    figlet = pyfiglet.Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid font name")
    else:
        sys.exit("Usage: python figlet.py [-f FONTNAME]")
    text = input("Input: ")
    fig = pyfiglet.Figlet(font=font)
    print("Output:")
    print(fig.renderText(text))

main()

