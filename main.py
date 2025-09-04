"""Main entry point for the Snake game.

This script GLUES TOGETHER the different objects (instances of classes) that make up the game:
  * Screen (from turtle): window & rendering management.
  * Snake (our class): the moving snake composed of square segments.
  * Food (our class): a small circle the snake eats to grow.
  * Scoreboard (our class): displays current score and game over text.

GAME LOOP OVERVIEW (common in many games):
  1. Update visuals (screen.update()).
  2. Wait a short time to control speed (time.sleep()).
  3. Move game entities (snake.move()).
  4. Check for and handle collisions (food, walls, tail).
  5. Repeat until a game-over condition occurs.

Keyboard events let the player change direction; we bind arrow keys to snake methods.
"""

from turtle import Screen          # Turtle graphics window manager.
from snake import Snake             # Our Snake class (manages body segments & movement logic).
from food import Food               # Food class (random placement, appearance).
from scoreboard import Scoreboard   # Scoreboard class (handles score display & game over message).
import time                         # Used to slow down the game loop for consistent speed.

# -------------------- SCREEN SETUP -------------------- #
screen = Screen()                       # Create a single screen (window) instance.
screen.setup(width=600, height=600)     # Set fixed window size (coordinate system roughly -300..300).
screen.bgcolor("black")                 # Background for classic snake feel & contrast.
screen.title("My Snake Game")           # Window title bar text.
screen.tracer(0)                        # Turn off auto-refresh; we'll manually refresh for smoother animation.

# -------------------- OBJECT CREATION ----------------- #
snake = Snake()         # Build initial 3-segment snake.
food = Food()           # Create food and place at a random spot.
scoreboard = Scoreboard()  # Create score display at top.

# -------------------- INPUT HANDLERS ------------------ #
screen.listen()  # Start listening for key presses.
# Bind each arrow key to a method that changes the snake's heading.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# -------------------- MAIN GAME LOOP ------------------ #
game_is_on = True  # Control flag to stop the loop when game is over.
while game_is_on:
    screen.update()        # Redraw everything since last tracer(0) frame.
    time.sleep(0.1)        # Adjust speed (smaller = faster). 0.1s per frame.
    snake.move()           # Advance snake: body segments follow the one ahead; head moves forward.

    # --- Collision: Snake head with Food --- #
    # distance() returns Euclidean distance between two turtle objects.
    if snake.head.distance(food) < 15:  # 15 chosen because head size (~20) & food size (~10) => overlap threshold.
        food.refresh()           # Reposition food randomly.
        snake.extend()           # Add a new segment to tail.
        scoreboard.increase_score()  # Update score display.

    # --- Collision: Snake head with Wall --- #
    # Playable bounds: ~ -280..280 (allowing margin so head doesn't go off-screen before detection).
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()  # Write GAME OVER text.

    # --- Collision: Snake head with Own Tail --- #
    # If head touches any other segment: game ends.
    for segment in snake.segments[1:]:  # Iterate over all but the head.
        if snake.head.distance(segment) < 10:  # 10 works since segments are 20x20 squares.
            game_is_on = False
            scoreboard.game_over()

# Keep window open until user clicks inside it.
screen.exitonclick()
