# Description: A simple 10 PRINT maze generator in Python using Tkinter for visualization.
# The example is based on the 10 PRINT project, which explores the aesthetic of randomness in computer-generated patterns.
# The program generates a maze-like pattern by randomly choosing between two characters ("/" and "\") for each cell in the grid.
# The maze is displayed in a Tkinter window, with each cell represented by a character drawn on a canvas.   

# The speed of the animation can be adjusted by changing the delay in the window.after() function.  
# The program demonstrates a simple way to create visual patterns using randomness and basic graphics in Python.    
# We talked about that example in our first session. 
#
# The line 10 PRINT CHR$(205.5+RND(1)); : GOTO 10 is a BASIC program and a classic one-liner from early computing.
# famously used on the Commodore 64, and it generates an endless maze-like pattern on the screen.
# For more see https://10print.org/, https://www.c64-wiki.de/wiki/PETSCII
# https://www.youtube.com/watch?v=bEyTZ5ZZxZs or for example https://github.com/net-art-uchicago/10print 
# another variation can be found on https://openprocessing.org/sketch/1051452. 
# Openprocessing offers a lot of examples for creative coding including 10 Print variations.

# Import the necessary libraries
import random
import tkinter as tk

# Set up the window
width = 40  # Number of characters wide
height = 20  # Number of characters tall
cell_size = 16  # Adjusted size of each character in pixels for better fit

# Initialize the tkinter window
window = tk.Tk()
window.title("10 PRINT Maze Generator")
canvas = tk.Canvas(window, width=width * cell_size, height=height * cell_size, bg="black")
canvas.pack()

current_row = 0  # Start at the top row

# Function to draw one line at a time, similar to the original 10 PRINT
def draw_maze():
    global current_row

    # Draw the current row with random slashes
    for col in range(width):
        char = random.choice(["\\", "/"])
        color = "white" if char == "\\" else "cyan"

        # Draw each character in its position
        canvas.create_text(col * cell_size, current_row * cell_size,
                           text=char, fill=color, font=("Courier New", cell_size), anchor="nw")

    # Move to the next row, wrapping to the top if at the bottom
    current_row += 1
    if current_row >= height:
        current_row = 0
        canvas.delete("all")  # Clear the canvas once we reach the end, like a reset

    # Schedule the function to run again for continuous animation
    window.after(200, draw_maze)

# Start the animation
draw_maze()
window.mainloop()
