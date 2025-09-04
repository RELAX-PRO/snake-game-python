"""Food module.

The Food class represents the collectible item the snake eats to grow.
It appears as a small blue circle and jumps to a new random position each time it's eaten.
"""

from turtle import Turtle  # Base class (for shape, movement, drawing capabilities).
import random               # Used for random coordinate selection.


class Food(Turtle):
    """A small circle the snake aims to collide with."""

    def __init__(self):
        super().__init__()                     # Initialize Turtle state.
        self.shape("circle")                   # Circle shape (default, but explicit is clear).
        self.penup()                           # Disable drawing lines when moving.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Shrink to half (default size is 20x20 -> now ~10x10).
        self.color("blue")                     # Distinct color.
        self.speed("fastest")                  # Instant movement when repositioned.
        self.refresh()                         # Place at random starting position.

    def refresh(self):
        """Move the food to a random on-screen location within play bounds."""
        random_x = random.randint(-280, 280)    # Horizontal coordinate.
        random_y = random.randint(-280, 280)    # Vertical coordinate.
        self.goto(random_x, random_y)           # Teleport to new location.
