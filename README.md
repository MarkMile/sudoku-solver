# Sudoku Solver

A visual Sudoku solver built with Python and CustomTkinter, featuring a clean modern interface, puzzle validation, and a step-by-step solving visualization powered by a backtracking algorithm.

Designed for Sudoku enthusiasts who enjoy both playing and understanding how puzzles can be solved programmatically.

## 💡 Project Motivation
I’ve always enjoyed solving Sudoku puzzles — and so does my wife.

This project started as a fun way for us to combine that shared interest with my love for programming.

It became a great learning exercise in algorithm design, GUI development, and writing clean, modular Python code while building something enjoyable and interactive.

## 🚀 Features
- 🖥️ Modern GUI with CustomTkinter – sleek, responsive, and user-friendly
- 🧠 Backtracking Algorithm – solves puzzles efficiently and recursively
- 🧾 Input Validation – checks if the entered puzzle follows Sudoku rules
- 🔘 Solve & Reset Buttons – simple and clean controls
- 💡 Modular Codebase – clearly separated logic, GUI, and validation components

## 🧩 How It Works
This program uses a backtracking algorithm, a depth-first search technique that:

- Finds the first empty cell.
- Tries numbers 1–9.
- Checks if a placement is valid (no duplicates in row, column, or 3×3 box).
- Continues recursively until the puzzle is solved or backtracks when stuck.

## 🖥️ Technologies Used
- **Python** 3.x
- **Tkinter** – for GUI backend
- **CustomTkinter** – modern UI framework for Python (built on top of Tkinter)
- **Algorithmic backtracking** – for puzzle solving

## 🗂️ Project Structure

`sudoku-solver/`<br>
`│`<br>
`├── main.py             # Entry point; initializes the GUI and application`<br>
`├── sudoku_gui.py       # Handles all CustomTkinter GUI elements and layout`<br>
`├── solving_logic.py    # Contains the backtracking algorithm and solving logic`<br>
`├── input_validator.py  # Validates Sudoku inputs and ensures puzzle correctness`<br>
`└── README.md`<br>


## 📦 Installation
1. Clone the repository:<br>
    `git clone https://github.com/your-username/sudoku-solver.git`<br>
    `cd sudoku-solver`

2. Install dependencies<br>
    `pip install customtkinter`

3. Run the application<br>
    `python main.py`

## 🕹️ Controls
| Action               | Description                             |
| -------------------- | --------------------------------------- |
| 🖱️ **Click a cell** | Select a cell to input a number         |
| 🔢 **Enter number**  | Fill a value in the selected cell       |
| 🧩 **Solve**         | Automatically solves the current Sudoku |
| 🔁 **Reset**         | Clears all cells and resets the board   |

## 📷 Preview

## 🛠️ Future Improvements

- Sudoku puzzle generator
- Difficulty levels
- Timer and statistics
- Highlight conflicts and possible candidates
- Improved UI/UX with sound and animations

## 🧑‍💻 Author
#### **Marko Miletic**
