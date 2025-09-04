# Snake Game in Python

A classic Snake game implementation using Python's built-in `turtle` graphics library. This project demonstrates object-oriented programming principles with clean, well-documented code.

## 🎮 Game Features

- **Classic Snake Gameplay**: Control a growing snake to eat food and avoid collisions
- **Smooth Graphics**: Built with Python's turtle graphics for clean visuals
- **Score Tracking**: Real-time score display that increases as you eat food
- **Collision Detection**: 
  - Wall boundaries
  - Self-collision (snake hitting its own tail)
  - Food collection
- **Responsive Controls**: Arrow key navigation with 180° turn prevention
- **Game Over Screen**: Clear indication when the game ends

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- tkinter (usually included with Python installations)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/RELAX-PRO/snake-game-python.git
cd snake-game-python
```

2. No additional dependencies needed! The game uses only Python's built-in modules.

### Running the Game

```bash
python main.py
```

Or on some systems:
```bash
python3 main.py
```

## 🎯 How to Play

### Controls
- **↑ Arrow Key**: Move Up
- **↓ Arrow Key**: Move Down  
- **← Arrow Key**: Move Left
- **→ Arrow Key**: Move Right

### Game Rules
1. Use arrow keys to control the snake's direction
2. Eat the blue food circles to grow your snake and increase your score
3. Avoid hitting the walls or your own tail
4. The game ends when you collide with a boundary or yourself
5. Try to achieve the highest score possible!

### Gameplay Tips
- Plan your moves ahead to avoid getting trapped
- The snake cannot reverse directly into itself (180° turns are blocked)
- Each food item increases your score by 1 and adds a segment to your snake

## 🏗️ Code Structure

The project follows object-oriented design principles with clear separation of concerns:

### Core Modules

- **`main.py`** - Game coordinator and main loop
  - Sets up the game window and handles the game loop
  - Manages collision detection and game state
  - Coordinates between all game objects

- **`snake.py`** - Snake entity and movement logic
  - Manages snake segments and growth
  - Handles directional movement and input validation
  - Prevents invalid moves (like reversing into itself)

- **`food.py`** - Food item management
  - Randomly places food items on the game board
  - Handles food appearance and repositioning

- **`scoreboard.py`** - Score tracking and display
  - Displays current score and game over messages
  - Manages text rendering on the game screen

### Key Features of the Implementation

- **Modular Design**: Each class has a single responsibility
- **Encapsulation**: Game logic is properly encapsulated within classes
- **Clean Code**: Extensive comments and clear variable names
- **Constants**: Magic numbers are defined as named constants
- **Error Prevention**: Input validation prevents game-breaking moves

## 🎨 Game Screenshots

The game features:
- 600x600 pixel game window with black background
- White snake segments (20x20 pixel squares)
- Blue circular food items
- White score display at the top
- Clean, minimalist design for optimal gameplay

## 🛠️ Technical Details

- **Language**: Python 3.6+
- **Graphics**: turtle module (built-in)
- **Dependencies**: None (uses only Python standard library)
- **Architecture**: Object-oriented with inheritance
- **Game Loop**: Fixed timestep with collision detection
- **Input Handling**: Event-driven keyboard input

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Bug Reports**: Found a bug? Open an issue with details
2. **Feature Requests**: Have an idea? Share it in the issues
3. **Code Improvements**: Submit pull requests for enhancements
4. **Documentation**: Help improve this README or add code comments

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit with clear messages: `git commit -m "Add feature description"`
5. Push to your fork: `git push origin feature-name`
6. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Future Enhancements

Potential improvements for future versions:
- High score persistence
- Different difficulty levels (speed settings)
- Sound effects
- Different food types with varying point values
- Pause/resume functionality
- Colorful themes and customization options

## 🐍 About

This Snake game was created as a demonstration of object-oriented programming in Python. It showcases clean code practices, proper class design, and effective use of Python's built-in libraries to create an engaging game experience.

---

**Enjoy playing Snake! 🐍**