# ------------------------------------
# GUI: CustomTkinter application class
# ------------------------------------

from PIL import Image
import customtkinter as ctk
from typing import List, Tuple

from solving_logic import SudokuSolver
from input_validator import InputValidator


class GUI(ctk.CTk):
    """Sudoku Solver graphical user interface."""

    def __init__(self) -> None:
        """GUI initialization and configuration."""
        super().__init__()
        self.title("Sudoku puzzle solver")
        self.resizable(False, False)
        self.configure(fg_color="#1b1d28")

        # Board size
        self.number_of_rows: int = 9
        self.number_of_cols: int = 9

        # State flag and data
        self.is_solved: bool = False
        self.sudoku_board: List[List[ctk.CTkEntry]] = []
        self.sudoku_puzzle: List[List[int]] = [[0] * 9 for _ in range(9)]

        # Layout frames
        self._build_frames()

        # Create components
        self.message_box: ctk.CTkLabel = self._create_message_box()
        self.frame_for_buttons: ctk.CTkFrame = self._create_buttons_frame()

        # Validator and solver
        self.validator: InputValidator = InputValidator(lambda: self.is_solved)
        # The registered Tkinter callback must return a boolean; we bridge it below.
        self._register_validator_callback()

        self.create_sudoku_board()

        self.solve_button: ctk.CTkButton = self.create_solve_button()
        self.reset_button: ctk.CTkButton = self.create_reset_button()

        # Solver instance (will be given the puzzle before solving)
        self.solver: SudokuSolver = SudokuSolver()

    def _build_frames(self) -> None:
        """Create and place the main frames for the board and control buttons."""
        self.board_frame: ctk.CTkFrame = ctk.CTkFrame(
            master=self, fg_color="transparent"
        )
        self.board_frame.grid(row=1, column=0, padx=50, pady=25)

    def _create_message_box(self) -> ctk.CTkLabel:
        """
        Create a message box (label) which is used to show user feedback.

        :return message_box: (CTkLabel) - Configured and positioned message box.
        """
        message_box: ctk.CTkLabel = ctk.CTkLabel(
            master=self,
            height=45,
            width=410,
            corner_radius=30,
            fg_color="#222533",
            text_color="#cacbcc",
            text="Welcome to Sudoku puzzle solver.",
            font=ctk.CTkFont(family="Calibri", size=18, weight="normal"),
        )
        message_box.grid(row=0, column=0, pady=(30, 0))
        return message_box

    def _create_buttons_frame(self) -> ctk.CTkFrame:
        """
        Create a frame which will hold 'Solve' and 'Reset' buttons.

        :return buttons_frame: (CTkFrame) - Frame to hold 'Solve' and 'Reset' buttons.
        """
        buttons_frame: ctk.CTkFrame = ctk.CTkFrame(master=self, fg_color="transparent")
        buttons_frame.grid(row=2, column=0, padx=50, pady=(0, 40))
        return buttons_frame

    # ----- validation bridge -----
    def _register_validator_callback(self) -> None:
        """
        Register a wrapper that bridges Tkinter's validatecommand to the validator.
        The callback used in CTkEntry.validatecommand must be a Tcl wrapper returned by `register`.
        """
        self._tcl_validate: str = self.register(self._validate_and_feedback)

    def _validate_and_feedback(self, new_value: str) -> bool:
        """
        Bridge between the SudokuInputValidator and the CTkEntry validatecommand.
        It updates the message_box with the returned message.

        :param new_value: (str) - Value that the user typed into the square.
        :returns is_valid: (bool) - True if the users value is valid (number from 1 to 9), otherwise False.
        """
        is_valid, message = self.validator.validate(new_value)
        if message:
            self.message_box.configure(text=message)
        return is_valid

    # ----- creation helpers -----
    def create_sudoku_board(self) -> None:
        """Create and place 9x9 CTkEntry fields inside board_frame."""
        # Clear previous data (if any) before creating the board.
        self.sudoku_board: List[List[ctk.CTkEntry]] = []

        for i in range(self.number_of_rows):
            row_widgets: List[ctk.CTkEntry] = []
            for j in range(self.number_of_cols):
                sudoku_square: ctk.CTkEntry = self.create_sudoku_square()

                # Add extra padding between 3x3 boxes for clearer grid visuals.
                # CTkEntry.grid accepts either int or tuple for padx/pady.
                pad_x: Tuple[int, int] | int = (3, 9) if j in (2, 5) else 3
                pad_y: Tuple[int, int] | int = (3, 9) if i in (2, 5) else 3

                sudoku_square.grid(row=i, column=j, padx=pad_x, pady=pad_y)

                row_widgets.append(sudoku_square)
            self.sudoku_board.append(row_widgets)

    def create_sudoku_square(self) -> ctk.CTkEntry:
        """
        Create a single CTkEntry configured for Sudoku digits with validation.

        :return sudoku_square: (CTkEntry) - Configured Sudoku square with validation.
        """
        sudoku_square: ctk.CTkEntry = ctk.CTkEntry(
            master=self.board_frame,
            width=40,
            height=40,
            border_width=1,
            justify="center",
            fg_color="#222533",
            text_color="#7d8093",
            border_color="#2e3245",
            font=ctk.CTkFont(family="Calibri", size=20, weight="normal"),
        )

        # validatecommand expects a tuple (callback, substitution_codes...)
        sudoku_square.configure(
            validate="key", validatecommand=(self._tcl_validate, "%P")
        )
        return sudoku_square

    def create_solve_button(self) -> ctk.CTkButton:
        """
        Create the Solve button that triggers puzzle solving.

        :returns solve_button: (CTkButton) - Configured 'Solve' button.
        """
        solve_button: ctk.CTkButton = ctk.CTkButton(
            master=self.frame_for_buttons,
            width=200,
            height=40,
            text=" Solve",
            corner_radius=20,
            fg_color="#7132c1",
            hover_color="#3f1c6c",
            font=ctk.CTkFont(family="Calibri", size=18, weight="normal"),
            command=self.attempt_to_solve,
        )
        solve_button.grid(row=0, column=0)
        return solve_button

    def create_reset_button(self) -> ctk.CTkButton:
        """
        Create the reset button with a themed icon.

        :return reset_button: (CTkButton) - Configured 'Reset' button.
        """
        reset_icon: ctk.CTkImage = ctk.CTkImage(
            light_image=Image.open("./icons/reset.png"),
            dark_image=Image.open("./icons/reset.png"),
            size=(25, 25),
        )

        reset_button: ctk.CTkButton = ctk.CTkButton(
            master=self.frame_for_buttons,
            text="",
            width=50,
            height=50,
            image=reset_icon,
            border_width=1,
            corner_radius=30,
            fg_color="#222533",
            hover_color="#2e3245",
            border_color="#2e3245",
            command=self.reset_the_board,
        )
        reset_button.grid(row=0, column=1, padx=(10, 0))
        return reset_button

    # ----- user interactions & board sync -----
    def get_user_inputs(self) -> None:
        """Read current CTkEntry values and populate self.sudoku_puzzle with ints."""
        for i in range(self.number_of_rows):
            for j in range(self.number_of_cols):
                value: str = self.sudoku_board[i][j].get().strip()
                self.sudoku_puzzle[i][j] = int(value) if value.isdigit() else 0

    def mark_user_inputs(self) -> None:
        """Style fields where the user entered values to visually distinguish them."""
        for i in range(self.number_of_rows):
            for j in range(self.number_of_cols):
                square: ctk.CTkEntry = self.sudoku_board[i][j]
                if square.get().strip() != "":
                    square.configure(fg_color="#1b1d28")

    def fill_the_board(self) -> None:
        """Fill all CTkEntry widgets from self.sudoku_puzzle (overwrite existing text)."""
        for i in range(self.number_of_rows):
            for j in range(self.number_of_cols):
                entry: ctk.CTkEntry = self.sudoku_board[i][j]
                entry.delete(0, "end")
                entry.insert(0, str(self.sudoku_puzzle[i][j]))

    def reset_the_board(self) -> None:
        """Reset the board to an empty state and reset styles/messages."""
        self.is_solved: bool = False
        self.sudoku_puzzle: List[List[int]] = [[0] * 9 for _ in range(9)]

        for i in range(self.number_of_rows):
            for j in range(self.number_of_cols):
                square: ctk.CTkEntry = self.sudoku_board[i][j]
                square.delete(0, "end")
                square.configure(fg_color="#222533", border_color="#2e3245")

        self.message_box.configure(text="Fill the board with your numbers.")

        # Focus first cell for convenience
        if self.sudoku_board and self.sudoku_board[0]:
            self.sudoku_board[0][0].focus()

    # ----- solver integration -----
    def are_valid_positions(self) -> bool:
        """
        Validate that non-empty user-entered positions are consistent.

        :returns bool: True if all user-entered numbers are placed validly, otherwise False.
        """
        for r in range(self.number_of_rows):
            for c in range(self.number_of_cols):
                value: int = self.sudoku_puzzle[r][c]
                if value != 0:
                    if not self.solver.is_valid_position(value, (r, c)):
                        # Provide a concise message to the user; solver does not set messages.
                        self.message_box.configure(
                            text=f"Invalid placement detected (row {r+1}, column {c+1})."
                        )
                        return False
        return True

    def attempt_to_solve(self) -> None:
        """Collect inputs, validate positions, run solver, and update UI."""
        if self.is_solved:
            self.message_box.configure(text="Already solved. Please reset the board.")
            return

        self.get_user_inputs()
        # Sync solver puzzle and validate
        self.solver.set_puzzle(self.sudoku_puzzle)

        if not self.are_valid_positions():
            return

        # Run the solver
        solved: bool = self.solver.solve()
        if solved:
            self.sudoku_puzzle = [row[:] for row in self.solver.puzzle]
            self.mark_user_inputs()
            self.fill_the_board()
            self.is_solved = True
            self.message_box.configure(text="Solved!")
        else:
            self.message_box.configure(text="No solution found...")

    # ---- utility to run the app ----
    def run(self) -> None:
        self.mainloop()
