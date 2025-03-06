from path import *
from typing import *


class Board:
    """
    A class representing a board object in the game boggle
    Attributes:
    board (List[List[str]]) : the board of the game.
    path (class Path) : the current path being created on the board.
    prefix (str) : the current prefix that's created from the current path on board.
    dict_path_n (Dict[int:List[List[Tuple[int, int]]]]) : a dictionary that holds
    the current found paths (as a list of tuples). The keys are n; the length of the
    paths, and the values are the list of the paths (a list of lists of tuples)
    dict_word_n (Dict[int:List[List[Tuple[int, int]]]]) : a dictionary that holds
    the current found paths (as a list of tuples). The keys are n; the length of the
    words, and the values are the list of the paths (a list of lists of tuples)
    dict_found_words (Dict[str:List[Tuple[int, int]]]) : a dictionary that holds the
    current max paths that create each found word. The keys are the found word,
    the values are the longest path creating that word. Each key only has one value
    """
    def __init__(self, board: List[List[str]]):
        """
        constructor for board object - creates the board,
        an empty "path" which represents the current path,
        the prefix of that path as an empty string, and empty dictionaries.
        :param : board: two-dimensional list representing a board of letters
        """
        self.__board = board
        self.__path = Path()
        self.__prefix = ""
        self.__dict_path_n = dict()
        self.__dict_word_n = dict()
        self.__dict_found_words = dict()

    def __str__(self) -> str:
        """
        a function used to print out the board.
        :return: inclusive string of the board
        """
        print_board = ""
        for row in range(len(self.__board)):
            print_board = print_board + "\n"
            # after each line ends add to the variable of the resulted string a "\n"
            for column in range(len(self.__board[row])):
                print_board = print_board + "[" + str(self.__board[row][column]) + "] "
                # for each cell add to the resulted string a representation
                # of that cell in the shape of "[<letter_sequence>]"
        return print_board

    def cell_list_empty(self) -> List[Tuple[int, int]]:
        """
        :return: all coordinates on board that aren't used in current path
        """
        lst_cells = []
        for row in range(len(self.__board)):
            for column in range(len(self.__board[row])):
                if (row, column) not in self.__path.get_cords():
                    lst_cells.append((row, column))
                # add every cell on the board to the lst_cells if it is not
                # part of the current path
        return lst_cells

    def possible_moves(self, word: str = None) -> List[Tuple[int, int]]:
        """
        check what coordinates can possibly be added to the path to eventually
        form the desired word (the input)
        :param word: represents the word to be created in the board (if possible)
        :return: list of coordinates on board around the previous coordinate, that carry a valid
        sequence of letters (a prefix of the suffix of a given word)
        """
        possible_moves = list()
        # possible_moves will hold all the coordinates that can potentially form the
        # desired word
        if word:
            # if you are looking for certain word on board
            suffix = word[len(self.__prefix):]
            # suffix will hold the remaining part of the desired word that has
            # yet to be found
            if self.__path.possible_moves() == "All":
                for coordinate in self.cell_list_empty():
                    if suffix.startswith(self.__board[coordinate[0]][coordinate[1]]):
                        # if any move on the board is possible, go through every one
                        # and add those that contain the prefix to possible_moves
                        possible_moves.append(coordinate)
            else:
                for coordinate in self.__path.possible_moves():
                    if coordinate in self.cell_list_empty() and suffix.startswith(self.__board[coordinate[0]][coordinate[1]]):
                        # for every possible move, check if the cell contains the required prefix
                        # and that it is free. If so, add this coordinate to possible_moves
                        possible_moves.append(coordinate)
        else:
            # if you want to return all the possible moves, not dependent on a specific word
            if self.__path.possible_moves() == "All":
                # if all the moves are possible for the current path,
                # return all the empty cells on board
                return self.cell_list_empty()
            else:
                for coordinate in self.__path.possible_moves():
                    # otherwise, add the valid moves that are 'empty' coordinates to possible_moves
                    if coordinate in self.cell_list_empty():
                        possible_moves.append(coordinate)
        return possible_moves

    def extend_path(self, cord: Tuple[int, int]) -> bool:
        """
        extends the current path on the board if possible
        :param cord: a coordinate on board (or not)
        :return: boolean value, representing if the extension was successful or not
        """
        if cord in self.possible_moves():
            self.__path.add_cord(cord)
            self.__prefix = self.__prefix + self.__board[cord[0]][cord[1]]
            return True
        return False

    def shorten_path(self) -> Tuple[int, int] or None:
        """
        shortens the path by one
        """
        if not self.__path.get_cords():
            return
        # if the path is empty do nothing
        # else: shorten the path and update qualities accordingly
        cord_removed = self.__path.remove_last()
        self.__prefix = self.__prefix[:-(len(self.__board[cord_removed[0]][cord_removed[1]]))]
        # removed the last appended coordinate from the current path
        # remove the previously added letters from the end of the prefix
        return cord_removed

    def get_word(self) -> str:
        """
        :return: the prefix created by current path on board
        """
        return self.__prefix

    def get_path(self) -> Path:
        """
        :return: the current path on board
        """
        return self.__path

    def initialize_path(self) -> None:
        """resets the current path and the prefix created by it on board"""
        self.__path = Path()
        self.__prefix = ""

    def find_word_on_board(self, word: str) -> None:
        """
        this method finds all the different existing paths to create a specific
        word (its input). The paths are stored in multiple different dictionaries,
        all for different purposes
        :param word: a word given to find on board
        :return: None. function only updates dictionaries of board.
        """
        path_coordinates = self.get_path().get_cords()
        # variable holds the coordinates of the path in list
        path_length = self.get_path().get_length()
        # variable holds the length of the path
        # BASE CASE!
        if self.__prefix == word:
            # if current prefix on board is the word, map to the dictionaries accordingly:
            if word not in self.__dict_found_words or path_length > len(self.__dict_found_words[word]):
                self.__dict_found_words[word] = path_coordinates[:]
                # if the word wasn't found yet, or the path currently found is longer than
                # the path currently held for "word", update value in dictionary
            if len(word) not in self.__dict_word_n:
                # if key for the current path length doesn't exist - create it with empty list
                self.__dict_word_n[len(word)] = []
            self.__dict_word_n[len(word)].append(path_coordinates[:])
            # add a copy of the path coordinates to the dictionary at the correct key.
            # key (key= n -> length of word)
            if self.get_path().get_length() not in self.__dict_path_n:
                # if key for the current word length doesn't exist - create it with empty list
                self.__dict_path_n[self.get_path().get_length()] = []
            self.__dict_path_n[self.get_path().get_length()].append(self.get_path().get_cords()[:])
            # add a copy of the path coordinates to the dictionary at the correct key.
            # key (key= n -> length of path)
        else:
            valid_moves = self.possible_moves(word)
            # variable holds all valid next moves on board in order to continue to
            # create "word" from current board status
            for move in valid_moves:
                self.extend_path(move)
                # try to extend
                self.find_word_on_board(word)
                # call recursively to continue to build the word
                self.shorten_path()
                # BACKTRACKING <3

    def get_paths_length_n(self, n: int) -> List[List[Tuple[int, int]]]:
        """
        :param n: represents length of paths
        :return: all paths in the length of n currently saved in dictionary
        """
        if n in self.__dict_path_n:
            return self.__dict_path_n[n]
        else:
            return []

    def get_words_length_n(self, n: int) -> List[List[Tuple[int, int]]]:
        """
        :param n: represents length of words
        :return: all paths of words in the length of n currently saved in dictionary
        """
        if n in self.__dict_word_n:
            return self.__dict_word_n[n]
        else:
            return []

    def get_high_score(self) -> List[List[Tuple[int, int]]]:
        """
        :return: list of all the maximal paths of each word currently found on board
        """
        return list(self.__dict_found_words.values())

    def get_found_words(self) -> List[str]:
        """
        :return: list of all found words on board
        """
        return list(self.__dict_found_words.keys())

    def get_board(self) -> List[List[str]]:
        """
        :return: the board filled with letters (in the form of two-dimensional list and not class object)
        """
        return self.__board




