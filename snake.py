"""Snake module.

Defines the Snake class which manages:
  * Initial creation of the snake body.
  * Movement (each segment following the one ahead of it).
  * Growth (adding new segments when food is eaten).
  * Direction changes with safety checks to block 180° reversals.

OOP Principle: Encapsulation
  All logic related to how a snake works is inside this class. The rest of the program only
  interacts with it via public methods (move, extend, up, down, left, right) without needing
  to know internal details (like how segments are stored).
"""

from turtle import Turtle  # Each segment is an independent Turtle instance.

# -------------------- CONSTANTS -------------------- #
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Three starting blocks horizontally.
MOVE_DISTANCE = 20  # Move in 20-pixel steps so it aligns with segment size (grid-like motion).
UP = 90             # Turtle heading angle constants.
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Represents the entire snake as an ordered list of square segments."""

    def __init__(self):
        self.segments = []          # List of Turtle objects (index 0 is the head).
        self.create_snake()         # Build initial snake body.
        self.head = self.segments[0]  # Store a direct reference to head for convenience.

    def create_snake(self):
        """Create initial snake from predefined positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Create a new segment at a specific position and append it to the snake."""
        new_segment = Turtle("square")  # Square visual for classic snake.
        new_segment.color("white")      # Set segment color.
        new_segment.penup()              # Avoid drawing lines between moves.
        new_segment.goto(position)       # Place segment.
        self.segments.append(new_segment)

    def extend(self):
        """Add a segment to the tail using the position of the last segment.

        On the next move() call, the normal follow logic places it correctly behind the snake.
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward one step.

        Process (iterate backwards):
          - Each segment takes the (x,y) of the one in front of it.
          - Finally, the head moves forward by MOVE_DISTANCE in its current heading.
        Going backwards prevents overwriting positions we still need to read.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from tail towards head (excluding head).
            new_x = self.segments[seg_num - 1].xcor()  # x of previous segment.
            new_y = self.segments[seg_num - 1].ycor()  # y of previous segment.
            self.segments[seg_num].goto(new_x, new_y)   # Jump segment to that position.
        self.head.forward(MOVE_DISTANCE)               # Move head forward by fixed distance.

    # Direction control methods: prevent 180° reversal which would cause instant self-collision.
    def up(self):
        if self.head.heading() != DOWN:  # Only change if not currently moving down.
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
