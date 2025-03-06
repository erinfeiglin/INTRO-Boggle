from foundwordsframe import *
from inputlineframe import *
from lettersframe import *
from startframe import *
from upperframe import *


class BoggleGame:
    """the main class that packs everything together. An instance of this class
    will start and run the game"""

    DISABLED_BUTTON_COLOR = "red"
    TIME_OUT = "00:00"
    GAME_NAME = "Boggle"
    ROOT_SIZE = "550x600"
    EMPTY_PREFIX = ""

    def __init__(self):
        root = tk.Tk()
        root.title(self.GAME_NAME)
        root.geometry(self.ROOT_SIZE)
        root.resizable(False, False)
        self._main_window = root
        self._upper_frame = UpperFrame(root)
        self._grid_frame = LettersFrame(root)
        self._user_input_frame = InputFrame(root)
        self._found_words_frame = FoundWordsFrame(root)
        self._start_menu = StartMenu(root)
        self._play_again_menu = EndMenu(root)
        self._list_of_scores = list()

    def _start_game(self):
        """this method is responsible for beginning the game
        it is the cmd given to the start button on the starting screen
        It creates all the needed frames, forgets/destroys the unnecessary frames/widgets
        and sets the buttons to have their commands"""
        self._create_frames()
        self._play_again_menu.forget_frame()
        self._start_menu.destroy_start_menu()
        self._check_time()
        self._grid_frame.set_buttons_cmd(self._push_letter)
        self._user_input_frame.set_backspace_cmd(self._push_backspace)
        self._user_input_frame.set_check_cmd(self._press_check_button)

    def _create_frames(self):
        """creates the needed frames (from the other classes)"""
        self._upper_frame.start_frame()
        self._grid_frame.start_frame()
        self._user_input_frame.start_frame()
        self._found_words_frame.start_frame()

    def _press_check_button(self):
        """this method is carried out when the "check" button is pressed
        it checks if the current string of letters creates a valid word
        If it is, the word is added to the found_words widget, the word's score is added
        to scoreboard, and the current word window is reset"""
        is_word = self._user_input_frame.get_curr_word()
        self._user_input_frame.set_curr_word(self.EMPTY_PREFIX)
        if (is_word in self._user_input_frame.get_dictionary() and is_word not in
                self._found_words_frame.get_found_words()):
            self._found_words_frame.add_to_found_words(is_word)
            curr_score = (self._grid_frame.get_board().get_path().get_length())**2
            self._upper_frame.add_to_score(curr_score)
        self._grid_frame.get_board().initialize_path()
        self._grid_frame.enable_all()

    def _push_letter(self, row, col):
        """this method is carried out when a letter button is pressed
        The button's value is added to the current word, and only the valid cells surrounding
        the chosen one are allowed to be clicked in the following turn """
        self._grid_frame.get_board().extend_path((row, col))
        self._user_input_frame.set_curr_word(self._user_input_frame.get_curr_word()+self._grid_frame.get_buttons()[row][col]["text"])
        self._grid_frame.disable_surrounding()
        self._grid_frame.get_buttons()[row][col].configure(state="disabled")
        self._grid_frame.get_buttons()[row][col]["bg"] = self.DISABLED_BUTTON_COLOR

    def _push_backspace(self):
        """this method is carried out when the backspace is pressed
        the previously added value is removed from the current word and the pressed button is unpressed"""
        if self._user_input_frame.get_curr_word() != self.EMPTY_PREFIX:
            row_removed, col_removed = self._grid_frame.get_board().shorten_path()
            if self._user_input_frame.get_curr_word():
                length_last = len(self._grid_frame.get_buttons()[row_removed][col_removed]["text"])
                self._user_input_frame.set_curr_word(self._user_input_frame.get_curr_word()[:-length_last])
            self._grid_frame.enable_all()
            if self._user_input_frame.get_curr_word():
                # disable the buttons from last turn
                self._grid_frame.disable_surrounding()
            for row_i, col_i in self._grid_frame.get_board().get_path().get_cords():
                # disable the buttons that make up the current path
                self._grid_frame.get_buttons()[row_i][col_i].configure(state="disabled")
                self._grid_frame.get_buttons()[row_i][col_i]["bg"] = self.DISABLED_BUTTON_COLOR

    def _forget_widgets(self):
        """this method makes all the widgets and frame be forgotten. it is used when
        the current game is over, as a means to reset the game
        it also creates a widget containing the final score and presents the user
        with the play again menu"""
        self._play_again_menu.create_final_score_widget(self._upper_frame.get_score())
        self._list_of_scores.append(int(self._upper_frame.get_score()))
        self._play_again_menu.create_high_score_widget(str(max(self._list_of_scores)))
        self._upper_frame.forget_widgets()
        self._grid_frame.forget_frame()
        self._user_input_frame.forget_widgets()
        self._found_words_frame.forget_widgets()
        self._play_again_menu.set_play_button_cmd(self._start_game)
        self._play_again_menu.present_widgets()

    def _check_time(self):
        """checks the current time on the timer
        if it has reached 0:00, the game is over, and the method
        forget_widgets is called"""
        if self._upper_frame.get_time() == self.TIME_OUT:
            self._forget_widgets()
        else:
            self._main_window.after(1000, self._check_time)

    def run(self):
        """the method used to run the game"""
        self._start_menu.set_start_button_cmd(self._start_game)
        self._main_window.mainloop()


a = BoggleGame()
a.run()
