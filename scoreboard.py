"""Scoreboard module.

Defines the Scoreboard class which inherits from turtle.Turtle so it can draw text directly
on the screen. It keeps track of the current score and displays a GAME OVER message when needed.

OOP Concept: Inheritance
  Scoreboard IS-A specialized Turtle. We reuse methods like write(), goto(), color(), etc.
"""

from turtle import Turtle  # Import base class we are extending.

# Constants for formatting. Using ALL_CAPS signals these shouldn't change at runtime.
ALIGNMENT = "center"  # How text is aligned relative to its (x, y) anchor position.
FONT = ("Courier", 24, "normal")  # (font family, size, style)


class Scoreboard(Turtle):
    """A simple text-based score tracker drawn at the top of the window."""

    def __init__(self):
        super().__init__()         # Initialize base Turtle internal state.
        self.score = 0             # Instance attribute storing current score value.
        self.color("white")        # Set pen (text) color.
        self.penup()               # Prevent drawing lines when repositioning.
        self.goto(0, 270)          # Start near top edge of 600x600 window.
        self.hideturtle()          # Hide the arrow / square icon; we just want text.
        self.update_scoreboard()   # Render initial score.

    def update_scoreboard(self):
        """Draw (or redraw) the current score value."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display a centered GAME OVER message."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score and refresh the scoreboard display.

        clear() erases only this turtle's drawings, avoiding overlap of new text over old text.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
