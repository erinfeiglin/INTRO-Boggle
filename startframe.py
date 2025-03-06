import tkinter as tk


class StartMenu:
    """this class is responsible for creating the start screen/menu"""

    SMALL_TEXT = ("Courier", 20)
    BIG_TEXT = ("Courier", 30)
    PADDING = 4
    GREEN = "green"

    def __init__(self, root):
        self._main_window = root
        self._welcome = tk.Label(root, text="welcome to boggle!", font=self.BIG_TEXT)
        self._welcome.pack(side="top", fill=tk.X, expand=True)
        self._start_button = tk.Button(root, text="start", bg=self.GREEN, font=self.SMALL_TEXT)
        self._start_button.pack(side="top", pady=self.PADDING)

    def destroy_start_menu(self):
        """this method destroys the start menu's widgets. it is called at the
        beginning of the game"""
        self._start_button.destroy()
        self._welcome.destroy()

    def set_start_button_cmd(self, cmd):
        """this method is responsible for giving the start button its command
        it is called when the game is run"""
        self._start_button.configure(command=cmd)


class EndMenu:
    """this class is responsible for creating the end screen, when the game is over"""

    DEFAULT_TEXT = ("Courier", 30)
    END_GAME_MESSAGE = "You finished the game!" + "\n" + "your score was: "
    PADDING = 4
    GREEN = "green"

    def __init__(self, root):
        self._main_window = root
        self._score_display_end = tk.Label(root)
        self._high_score_display = tk.Label(root)
        self._play_again = tk.Button(self._main_window, text="play again", font=self.DEFAULT_TEXT, bg=self.GREEN)

    def forget_frame(self):
        """this method makes all the widgets and frame be forgotten. it is used when
        the user chooses to play again"""
        self._score_display_end.forget()
        self._high_score_display.forget()
        self._play_again.forget()

    def set_play_button_cmd(self, cmd):
        """this method is responsible for giving the play again button
        its command. it is called when the current game is over, and
        allows for the user to play again"""
        self._play_again.configure(command=cmd)

    def create_final_score_widget(self, score):
        """this method creates the widget that shows the user his final score"""
        self._score_display_end = tk.Label(self._main_window, text=(self.END_GAME_MESSAGE + score),
                                           font=self.DEFAULT_TEXT)

    def create_high_score_widget(self, high_score):
        """this method creates the widget that shows the user his overall high score"""
        self._high_score_display = tk.Label(self._main_window, text="High score: "+high_score, font=self.DEFAULT_TEXT)

    def present_widgets(self):
        """this method packs all the created widgets """
        self._play_again.pack(side="top")
        self._score_display_end.pack(side="top", pady=self.PADDING)
        self._high_score_display.pack(side="top", pady=self.PADDING)
