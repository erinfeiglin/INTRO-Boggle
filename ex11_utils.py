from typing import *
from path import *
import board2



Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    a function that checks if a given path is possible and creates a word on the board,
    the function will return the word creates if path is valid and None if not.
    """
    board_object = board2.Board(board)
    # create a board object from given board of letters
    for coordinate in path:
        # for each coordinate of given path, if it is possible to extend it in
        # the current board, extend it, if not, return None
        if not board_object.extend_path(coordinate):
            return
    if board_object.get_word() in words:
        return board_object.get_word()
        # if the path was created successfully; if it creates a word in the dictionary
        # return it, otherwise, return None
    else:
        return


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    function returns a list of all paths in board that create legal words and are in the length of n
    :param n: represents length of the paths
    :param board: a two-dimensional list filled with letters or sequences of letters representing a boggle board
    :param words: a dictionary of words
    :return: list of paths (not objects but lists of coordinates) in the length of n
    """
    if n == 0:
        return list()
    elif n == 1:
        lst_paths = list()
        board_object = board2.Board(board)
        for row, col in board_object.cell_list_empty():
            if board[row][col] in words:
                lst_paths.append([(row, col)])
        return lst_paths
    else:
        board_object = board2.Board(board)
        # create a board object from given board of letters
        for word in words:
            if len(word) >= n:
                board_object.find_word_on_board(word)
            board_object.initialize_path()
        # try to find each word longer than n, creating a path for each successfully found
        # word. when done, return only the paths of length n
        return board_object.get_paths_length_n(n)


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    function returns a list of all paths in board that create legal words in the length of n
    :param n: represents length of the words
    :param board: a two-dimensional list filled with letters or sequences of letters representing a boggle board
    :param words: a dictionary of words
    :return: list of paths (not objects but lists of coordinates) that create words in the length of n
    """
    board_object = board2.Board(board)
    # create a board object from given board of letters
    for word in words:
        if len(word) == n:
            board_object.find_word_on_board(word)
        board_object.initialize_path()
    # try to find each word of length n, creating a path for each successfully found
    # word. when done, return the found paths
    return board_object.get_words_length_n(n)


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    a function that returns all paths to receive max score in the given boggle board for given dictionary of words
    :param board: a two-dimensional list filled with letters or sequences of letters representing a boggle board
    :param words: a dictionary of words
    :return: a list of the maximal path found for each word that can be created on board
    """
    board_object = board2.Board(board)
    # create a board object from given board of letters
    for word in words:
        board_object.find_word_on_board(word)
        board_object.initialize_path()
    # find all the possible words on the board, then return the longest path
    # of each word, using the board object's method, get_high_score
    return board_object.get_high_score()







