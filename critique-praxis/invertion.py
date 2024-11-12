# This script is a simple example of how code and output can differ
# it uses the Figlet library that generates ASCII art from text, and it's only used if the being_lazy variable is True

from pyfiglet import Figlet # pip install pyfiglet if you don't have it

# Variable that determines if the output will be generated
being_lazy = True

# Function that generates ASCII art
def output():
    ascii_art = Figlet(font='slant')
    print(ascii_art.renderText("Not being lazy is amazing!"))

# If the being_lazy variable is True, the output function is called
if being_lazy:
    output()