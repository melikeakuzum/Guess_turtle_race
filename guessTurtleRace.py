import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
RAINBOW_COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']  # Rainbow colors

def get_user_guess():
    print("There will be 7 turtles racing with the following colors:")
    for i, color in enumerate(RAINBOW_COLORS, 1):
        print(f"{i}. {color}")
    
    while True:
        guess = input("Which color do you think will win? (Enter color name): ").lower()
        if guess in RAINBOW_COLORS:
            return guess
        else:
            print("Invalid color! Please choose a valid color.")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

# Get user's guess
user_guess = get_user_guess()

# Initialize the screen
init_turtle()

# Shuffle colors and select the first 7
random.shuffle(RAINBOW_COLORS)
colors = RAINBOW_COLORS[:7]

# Start the race
winner = race(colors)

# Check the winner and print the result
print(f"The race is over! The winning color is: {winner}")
if user_guess == winner:
    print("Congratulations, you guessed correctly! Win!")
else:
    print(f"Sorry, you lost. The correct color was {winner}. Lose!")

# Wait for 5 seconds and close the window
time.sleep(5)
