import tkinter as tk


def create_dictionary() -> set:
    """this function takes the txt file containing all the valid words
    and converts it into a set, to be used as a variable in the game"""
    list_of_words = set()
    with open("boggle_dict.txt") as dictionary:
        lines = dictionary.readlines()
        for line in lines:
            list_of_words.add(line.rstrip())
    return list_of_words


class InputFrame:
    """this class is responsible for the storing the current word, for checking
    if the word is viable, and for allowing the user to backspace if he pleases"""

    GRAY = "lightgray"
    SMALL_TEXT = ("Courier", 20)
    BIG_TEXT = ("Courier", 12)

    def __init__(self, root):
        self._words = create_dictionary()
        self._main_window = root
        self._user_input_frame = None
        self._curr_word = None
        self._check_button = None
        self._backspace = None

    def start_frame(self):
        """this method creates the necessary frame and widgets"""
        self._create_frame()
        self._create_widgets()

    def _create_frame(self):
        """this method creates the frame that will contain the widgets"""
        self._user_input_frame = tk.Frame(self._main_window)
        self._user_input_frame.pack(fill=tk.BOTH, expand=True)

    def _create_widgets(self):
        """this method creates and packs the widgets into the created frame.
        it creates a label widget that will contain the current turn's word,
        a button widget that when pressed will check if the found word is valid,
        and another button that when pressed, will remove the user's previous move"""
        self._curr_word = tk.Label(self._user_input_frame, text="", font=self.BIG_TEXT,
                                   width=20, bg=self.GRAY)
        self._curr_word.pack(side="left", fill=tk.BOTH, expand=True)
        self._check_button = tk.Button(self._user_input_frame, text="check", font=self.SMALL_TEXT)
        self._check_button.pack(side="left", fill=tk.BOTH, expand=True)
        self._backspace = tk.Button(self._user_input_frame, text="backspace", font=self.SMALL_TEXT)
        self._backspace.pack(side="left", fill=tk.BOTH, expand=True)

    def set_backspace_cmd(self, cmd):
        """a method used to set the backspace button's command (used in the
        main class; bogglegame, when starting the game)"""
        self._backspace.configure(command=cmd)

    def set_check_cmd(self, cmd):
        """a method used to set the check button's command (used in the
        main class; bogglegame, when starting the game)"""
        self._check_button.configure(command=cmd)

    def set_curr_word(self, some_text):
        """a method used to set the curr_word widget's text to the specific word/letters
        chosen by the user
        Used to update the current word when the board's buttons are pressed (including
        when the backspace button is pressed; to remove the previous move's letter(s))"""
        self._curr_word["text"] = some_text

    def get_dictionary(self):
        """a method used to return the words of the dictionary"""
        return self._words

    def get_curr_word(self):
        """a method used to return the current chosen word/letters"""
        return self._curr_word["text"]

    def forget_widgets(self):
        """this method makes all the widgets and frame be forgotten. it is used when
        the current game is over, as a means to reset the game"""
        self._user_input_frame.forget()
        self._curr_word.forget()
        self._check_button.forget()
        self._backspace.forget()
