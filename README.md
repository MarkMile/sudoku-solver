# Sudoku Solver (CustomTkinter)

A visual **Sudoku solver** built with **Python** and **CustomTkinter**, featuring a clean modern interface, puzzle validation, and a step-by-step solving visualization powered by a **backtracking algorithm**.

Designed for **Sudoku enthusiasts** who enjoy both playing and understanding how puzzles can be solved programmatically.

## Features
- **Modern GUI with CustomTkinter** – sleek, responsive, and user-friendly
- **Backtracking Algorithm** – solves puzzles efficiently and recursively
- **Input Validation** – checks if the entered puzzle follows Sudoku rules
- **Solve & Reset Buttons** – simple and clean controls
- **Modular Codebase** – clearly separated logic, GUI, and validation components

## How It Works
This program uses a backtracking algorithm, a depth-first search technique that:

- Finds the first empty cell.
- Tries numbers 1–9.
- Checks if a placement is valid (no duplicates in row, column, or 3×3 box).
- Continues recursively until the puzzle is solved or backtracks when stuck.

## Technologies Used
- **Python** 3.x
- **Tkinter** – for GUI backend
- **CustomTkinter** – modern UI framework for Python (built on top of Tkinter)
- **Pillow (PIL)** - for image loading or resizing
- **Algorithmic backtracking** – for puzzle solving

## Project Structure
```bash
sudoku-solver/
│
├── main.py             # Launches the app
├── sudoku_gui.py       # Handles CustomTkinter GUI
├── solving_logic.py    # Backtracking solver logic
├── input_validator.py  # Validates Sudoku inputs
│
├── icons/              # App icons
│   └── reset.png
├── screenshots/        # App screenshots
│   └── sudoku-solver-preview.gif
│
├── requirements.txt    # Project dependencies
└── README.md
```

## Installation
1. Clone the repository:<br>
```bash
git clone https://github.com/MarkMile/sudoku-solver.git
cd sudoku-solver
```
2. Install dependencies<br>
```bash
pip install customtkinter
pip install pillow
```
4. Run the application<br>
```bash
python main.py
```

## Controls
| Action               | Description                             |
| -------------------- | --------------------------------------- |
| **Click a cell** | Select a cell to input a number         |
| **Enter number**  | Fill a value in the selected cell       |
| **Solve**         | Automatically solves the current Sudoku |
| **Reset**         | Clears all cells and resets the board   |

## Preview

![empty board](https://github.com/MarkMile/sudoku-solver/blob/main/screenshots/sudoku-solver-preview.gif)<br>

## Author
**Marko Miletic**<br>
[LinkedIn](https://www.linkedin.com/in/marko1987/)
