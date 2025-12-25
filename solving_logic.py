# solving_logic.py
# Pure logic for solving a 9x9 Sudoku puzzle.

from typing import List, Tuple


class SudokuSolver:
    """Encapsulates the logic for solving a 9x9 Sudoku puzzle using backtracking algorithm."""

    def __init__(self, puzzle: List[List[int]] = None) -> None:
        """
        Initialization of the Sudoku puzzle represented as nested list of integers.

        :param puzzle: (List(List[int])) - 9x9 Sudoku puzzle.
        """
        self.rows = 9
        self.cols = 9
        self.puzzle = (puzzle if puzzle is not None else [[0] * 9 for _ in range(9)])

    def set_puzzle(self, puzzle: List[List[int]]) -> None:
        """
        Set a new Sudoku puzzle.

        :param puzzle: (List[List[int]]) - 9x9 Sudoku puzzle.
        """
        self.puzzle = [row[:] for row in puzzle]

    def find_empty_square(self) -> Tuple[int, int] | None:
        """
        Find first empty field and return its position (row, col) or None if there is no empty fields.

        :return (row, col) | None: (Tuple[int, int]) | None - Position of the empty square or None if no empty squares left.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.puzzle[row][col] == 0:  # 0 representss an empty square
                    return row, col
        return None

    def is_valid_position(self, number: int, position: Tuple[int, int]) -> bool:
        """
        Check if a number can be placed at the given position without violating Sudoku rules.

        :param number: (int) - The number that the user has entered into the square.
        :param position: (Tuple[int, int]) - Position of the number on Sudoku board (row, column)
        :return bool: True if the number can be placed at the given position, False otherwise.
        """
        row, col = position

        # Row check
        for c in range(self.cols):
            if self.puzzle[row][c] == number and c != col:
                return False

        # Column check
        for r in range(self.rows):
            if self.puzzle[r][col] == number and r != row:
                return False

        # Box check
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.puzzle[r][c] == number and (r, c) != position:
                    return False

        return True

    def solve(self) -> bool:
        """
        Solve the Sudoku puzzle using backtracking algorithm.

        :return bool: True if the puzzle is solved, False otherwise.
        """
        empty_square: None | Tuple[int, int] = self.find_empty_square()
        if not empty_square:
            return True

        row, col = empty_square
        for num in range(1, 10):
            if self.is_valid_position(num, (row, col)):
                self.puzzle[row][col] = num
                if self.solve():
                    return True
                self.puzzle[row][col] = 0

        return False
