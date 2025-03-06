import tkinter as tk


class FoundWordsFrame:
    """The class responsible for creating the frame that will contain the found words"""

    def __init__(self, root):
        self._main_window = root
        self._found_words_frame = None
        self._scrollbar = None
        self._display_found_words = None
        self._set_found_words = set()

    def start_frame(self):
        """this method creates the frame and widgets needed to store the found words"""
        self._create_frame()
        self._create_widgets()

    def _create_frame(self):
        """this method creates the frame that will contain the widgets"""
        self._found_words_frame = tk.Frame(self._main_window)
        self._found_words_frame.pack(fill=tk.BOTH, expand=True)

    def _create_widgets(self):
        """this method creates and packs the widgets into the created frame.
        it creates a text widget that will contain the found words and a scrollbar
        that will allow the user to see all his found words"""
        self._scrollbar = tk.Scrollbar(self._found_words_frame)
        self._scrollbar.pack(side="right", fill=tk.Y, expand=True)
        self._display_found_words = tk.Text(self._found_words_frame, yscrollcommand=self._scrollbar.set,
                                            state="disabled")
        self._display_found_words.pack(fill=tk.BOTH, expand=True)
        self._scrollbar.config(command=self._display_found_words.yview)

    def forget_widgets(self):
        """this method makes all the widgets and frame be forgotten. it is used when
        the current game is over, as a means to reset the game"""
        self._found_words_frame.forget()
        self._scrollbar.forget()
        self._display_found_words.forget()

    def add_to_found_words(self, word):
        """this method takes a word as an argument. it adds said word into the set
        of found words, and inserts the word visually into the text widget, to be
        displayed on screen"""
        self._set_found_words.add(word)
        self._display_found_words["state"] = "normal"
        self._display_found_words.insert(tk.END, word + "\n")
        self._display_found_words["state"] = "disabled"

    def get_found_words(self):
        """this method returns the set containing all the found words"""
        return self._set_found_words

