import tkinter as tk
from boggle_board_randomizer import *
from board2 import *


class LettersFrame:
    """this class is responsible for creating the visual of the actual board. it
    creates and stores the buttons with the specific letters, as gotten from the
    randomized board"""

    DEFAULT_TEXT = ("Courier", 14)
    DISABLED_BUTTON_COLOR = "red"
    DEFAULT_BUTTON_COLOR = "dark green"
    HEIGHT = 3
    WIDTH = 3

    def __init__(self, root):
        self._board = Board(randomize_board())
        self._buttons = list()
        self._main_window = root
        self._grid_frame = None

    def start_frame(self):
        """this method creates the necessary frame and widgets"""
        self._create_frame()
        self._create_buttons(self._board.get_board())

    def _create_frame(self):
        """this method creates the frame that will contain the widgets"""
        self._grid_frame = tk.Frame(self._main_window)
        self._grid_frame.pack(fill=tk.BOTH, expand=True)

    def _create_buttons(self, board):
        """this method is used to create all the board's letters,
         and will allow for the user to click on them"""
        for column in range(len(board[0])):
            self._grid_frame.columnconfigure(column, weight=1)
        for row in range(len(board)):
            self._grid_frame.rowconfigure(row, weight=1)
        for row, col in self._board.cell_list_empty():
            self._make_button(board[row][col], row, col)

    def _make_button(self, seq_letters, row, col):
        """this method creates an individual button at a specific coordinate
        used is the create_buttons method"""
        button = tk.Button(self._grid_frame, text=seq_letters, height=self.HEIGHT, width=self.WIDTH,
                           font=self.DEFAULT_TEXT, bg=self.DEFAULT_BUTTON_COLOR)
        button.grid_configure(row=row, column=col, sticky="swne")
        if len(self._buttons) - 1 == row:
            self._buttons[-1].append(button)
        else:
            self._buttons.append(list())
            self._buttons[-1].append(button)

    def set_buttons_cmd(self, cmd):
        """this method takes a cmd as input, and uses the
        method _set_button_cmd to give every button the board the desired command"""
        for index_row, button_row in enumerate(self._buttons):
            for index_col, button in enumerate(self._buttons[index_row]):
                self._set_button_cmd(index_row, index_col, cmd)

    def _set_button_cmd(self, row, col, cmd):
        """this method takes a coordinate and a cmd as input
        it sets the button at the given coordinate to have the input command"""
        self._buttons[row][col].configure(command=lambda: cmd(row, col))

    def get_board(self):
        """returns the game's board"""
        return self._board

    def get_buttons(self):
        """returns the game's buttons"""
        return self._buttons

    def enable_all(self):
        """this method switches all the letter buttons to be in an active state"""
        all_button_row = len(self._buttons)
        all_button_col = len(self._buttons[0])
        for row in range(all_button_row):
            for col in range(all_button_col):
                self._buttons[row][col].configure(state="normal")
                self._buttons[row][col]["bg"] = self.DEFAULT_BUTTON_COLOR

    def disable_surrounding(self):
        """this method is responsible for making the invalid buttons not active,
        making it so the user is not able to press them (the buttons not directly
        surrounding the chosen one, and any button already chosen within this turn)"""
        for index_row, row in enumerate(self._buttons):
            for index_col, button in enumerate(row):
                if (index_row, index_col) not in self._board.get_path().get_cords():
                    button.configure(state="normal")
                    button["bg"] = self.DEFAULT_BUTTON_COLOR
        not_possible_moves = [move for move in self._board.cell_list_empty() if move not in self._board.possible_moves()]
        for move in not_possible_moves:
            row, col = move
            self._buttons[row][col].configure(state="disabled")
            self._buttons[row][col]["bg"] = self.DISABLED_BUTTON_COLOR

    def forget_frame(self):
        """this method makes all the widgets and frame be forgotten. it is used when
        the current game is over, as a means to reset the game"""
        self._board = Board(randomize_board())
        self._buttons = list()
        self._grid_frame.forget()

