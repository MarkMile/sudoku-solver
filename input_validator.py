# input_validator.py
# This module defines the InputValidator class for validating Sudoku cell inputs.

from typing import Callable, Tuple


class InputValidator:
    """Encapsulates validation rules for a single Sudoku cell input."""

    ALLOWED_VALUES = set("123456789")
    MESSAGES = {
        "solved": "Sudoku is solved. Reset the board for new entries.",
        "empty": "Please enter your numbers.",
        "invalid": "'{value}' is not a number. Enter a number from 1 to 9.",
        "valid": "Number {value} added.",
        "silently_reject": "",
    }

    def __init__(self, is_solved_callback: Callable[[], bool]) -> None:
        """
        Initialize the InputValidator with a callback to check if the puzzle is solved.
        
        :param is_solved_callback: (Callable[[], bool]) True if the puzzle is solved, False otherwise.
        """
        self._is_solved: Callable[[], bool] = is_solved_callback

    def validate(self, user_input: str) -> Tuple[bool, str]:
        """
        Validate if the user input is a valid number from 1 to 9.

        :param user_input: (str) User input that needs to be validated.
        :return Tuple: (bool, str): A tuple where the first element is True if valid,
                False otherwise, and the second element is the feedback message for the user.
        """
        # Checking if the puzzle is already solved
        if self._is_solved():
            return False, self.MESSAGES["solved"]

        # Reject more-than-one-character inputs silently (Tkinter sends intermediate states).
        if len(user_input) > 1:
            return False, self.MESSAGES["silently_reject"]

        # Check if the user has deleted the number from a field.
        if user_input == "":
            return True, self.MESSAGES["empty"]

        # Checking if the input is a number from 1 to 9.
        if user_input not in self.ALLOWED_VALUES:
            return False, self.MESSAGES["invalid"].format(value=user_input)

        return True, self.MESSAGES["valid"].format(value=user_input)
