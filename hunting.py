import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Hunting Game")
screen.bgcolor("green")

# Create the hunter turtle
hunter = turtle.Turtle()
hunter.shape("turtle")
hunter.color("black")
hunter.penup()

# Create the prey turtle
prey = turtle.Turtle()
prey.shape("circle")
prey.color("purple")
prey.penup()
prey.goto(random.randint(-200, 200), random.randint(-200, 200))

# Define the hunter movement functions
def move_left():
    hunter.setheading(180)
    hunter.forward(10)

def move_right():
    hunter.setheading(0)
    hunter.forward(10)

def move_up():
    hunter.setheading(90)
    hunter.forward(10)

def move_down():
    hunter.setheading(270)
    hunter.forward(10)

# Define the collision function
def check_collision():
    if hunter.distance(prey) < 20:
        print("You caught the prey!")
        prey.goto(random.randint(-200, 200), random.randint(-200, 200))

# Set up the key bindings
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.listen()

# Main game loop
while True:
    check_collision()