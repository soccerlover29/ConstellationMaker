import turtle
import random
import tkinter as tk
from tkinter import simpledialog

# Function to draw stars at random positions with varying sizes
def draw_random_stars(num_stars):
    global star_positions
    star_positions = []
    star_turtle.clear()
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(2, 5)
        star_positions.append((x, y))
        star_turtle.goto(x, y)
        star_turtle.dot(size)
    return star_positions

# Function to draw a random constellation
def draw_random_constellation():
    num_stars_in_constellation = simpledialog.askinteger("Input", "Number of stars in the constellation:")
    if not num_stars_in_constellation:
        return

    if num_stars_in_constellation > len(star_positions):
        num_stars_in_constellation = len(star_positions)

    selected_stars = random.sample(range(len(star_positions)), num_stars_in_constellation)
    star_turtle.pendown()
    for i in range(len(selected_stars) - 1):
        star_turtle.goto(star_positions[selected_stars[i]])
        star_turtle.goto(star_positions[selected_stars[i+1]])
    star_turtle.penup()

# Function to clear the screen
def clear_screen():
    star_turtle.clear()

# Function to handle mouse clicks and draw custom constellations
def handle_click(x, y):
    closest_star = None
    min_distance = float('inf')
    for star_x, star_y in star_positions:
        distance = ((star_x - x) ** 2 + (star_y - y) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_star = (star_x, star_y)

    if closest_star:
        custom_stars.append(closest_star)
        star_turtle.goto(closest_star)
        if len(custom_stars) > 1:
            star_turtle.pendown()
            star_turtle.goto(custom_stars[-2])
            star_turtle.penup()

def start_custom_constellation():
    global custom_stars
    custom_stars = []
    screen.onclick(handle_click)

# Set up the main application window
root = tk.Tk()
root.title("Constellation Maker")

# Create a canvas for the turtle screen inside the tkinter window
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Attach the turtle screen to the tkinter canvas
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")

# Create a turtle for drawing stars
star_turtle = turtle.RawTurtle(screen)
star_turtle.hideturtle()
star_turtle.speed(0)
star_turtle.color("white")
star_turtle.penup()

star_positions = []
custom_stars = []

# Buttons for interactions
random_star_button = tk.Button(root, text="Generate Random Stars", command=lambda: draw_random_stars(100))
random_star_button.pack()

constellation_button = tk.Button(root, text="Generate Random Constellation", command=draw_random_constellation)
constellation_button.pack()

custom_constellation_button = tk.Button(root, text="Create Custom Constellation", command=start_custom_constellation)
custom_constellation_button.pack()

clear_button = tk.Button(root, text="Clear Screen", command=clear_screen)
clear_button.pack()

# Start the tkinter main loop
root.mainloop()
