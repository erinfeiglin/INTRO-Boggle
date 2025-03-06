import tkinter as tk


class UpperFrame:
    """this class is responsible for the upper frame of the game,
    where the current time and score are stored"""

    TIME_OUT = 0
    INITIAL_TIME = "03:00"
    DEFAULT_TEXT = ("Courier", 20)
    EMPTY_SCORE = "0"

    def __init__(self, root):
        self._main_window = root
        self._upper_frame = None
        self._timer = None
        self._scoreboard = None

    def start_frame(self):
        """this method creates the necessary frame and widgets
        it also activates the timer"""
        self._create_frame()
        self._create_widgets()
        self._main_window.after(1000, self._activate_timer)

    def _create_frame(self):
        """this method creates the frame that will contain the widgets"""
        self._upper_frame = tk.Frame(self._main_window)
        self._upper_frame.pack(fill=tk.BOTH, expand=True)

    def _create_widgets(self):
        """this method creates all the frame's widgets and packs them accordingly
        Specifically, the timer and the scoreboard widgets"""
        self._timer = tk.Label(self._upper_frame, text=self.INITIAL_TIME, font=self.DEFAULT_TEXT)
        self._timer.pack(side="left")
        self._scoreboard = tk.Label(self._upper_frame, text=self.EMPTY_SCORE, font=self.DEFAULT_TEXT)
        self._scoreboard.pack(side="right")

    def get_score(self):
        """returns the current score"""
        return self._scoreboard["text"]

    def add_to_score(self, score):
        """this method takes an integer, score, as input, and adds it to
        the current score, and updates the scoreboard on the screen"""
        curr_score = int(self._scoreboard["text"])
        curr_score += score
        curr_score = str(curr_score)
        self._scoreboard["text"] = curr_score

    def _activate_timer(self):
        """this method is responsible for the timer. it makes it start counting down
        from three minutes"""
        if self._timer["text"] != self.TIME_OUT:
            minutes = self._timer["text"][:2]
            seconds = self._timer["text"][3:]
            if int(seconds) != 0:
                seconds = int(seconds) - 1
                if seconds >= 10:
                    curr_time = minutes + ":" + str(seconds)
                else:
                    curr_time = minutes + ":" + "0" + str(seconds)
            else:
                minutes = int(minutes) - 1
                curr_time = "0" + str(minutes) + ":59"
            self._timer["text"] = curr_time
            self._main_window.after(1000, self._activate_timer)

    def get_time(self):
        """returns the current time of the timer"""
        return self._timer["text"]

    def reset_time(self):
        """resets the timer to three minutes"""
        self._timer["text"] = self.INITIAL_TIME

    def forget_widgets(self):
        """this method makes all the widgets and frame be forgotten. it is used when
        the current game is over, as a means to reset the game"""
        self._scoreboard.forget()
        self._upper_frame.forget()
        self._timer.forget()
