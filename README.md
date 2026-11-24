# Rock Paper Scissors (Python)

Rock Paper Scissors game built in Python. 

## Features

- Play multiple rounds against the computer
- Randomized computer moves using Python's `random` module
- Input validation: invalid entries are rejected and the user is re-prompted
- Case-insensitive input ("ROCK", "Rock", and "rock" all work)
- Score tracking across rounds with a final score summary
- Play-again loop

## How to Run

1. Make sure Python 3 is installed:
   ```
   python3 --version
   ```
2. Clone the repository:
   ```
   git clone https://github.com/AveC130/RockPaperScissors.git
   cd RockPaperScissors
   ```
3. Run the game:
   ```
   python3 RockPaperScissor.py
   ```

## How It Works

The program is split into separate functions for readability:

- `human()`: gets and validates the player's choice
- `computer()`: randomly selects the computer's choice
- `results()`: determines the outcome of each round
- `score()`: updates the running score
- `main()`: runs the game loop

## What I Practiced

- Modular programming
- Control flow (conditionals and loops)
- Input validation
- Randomization
- State management
- Debugging and problem-solving

## Future Improvements

- Best-of-N match mode
- Option to track win/loss/tie statistics

## AveC130
