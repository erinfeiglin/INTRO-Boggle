from typing import *


class Path:
    """
        A class representing a path made up of a list of coordinates.
        Attributes:
        list_of_cords (List[Tuple[int, int]]) : list of coordinates that
        represent a certain path (in a currently "infinite" board)
        length (int) : the length of the path
    """
    def __init__(self):
        """
        constructor for path object - creates an empty list of coordinates, and an initialized length (0)
        """
        self.__length: int = 0
        self.__list_of_cords: List = list()

    def get_cords(self) -> List[Tuple[int, int]]:
        """
        :return : the path itself, a list of coordinates
        """
        return self.__list_of_cords

    def get_length(self) -> int:
        """
        :return : the length of the path
        """
        return self.__length

    def possible_moves(self) -> str or List[Tuple[int, int]]:
        """
        checks what coordinates around the previous coordinate can lengthen the path (aren't already in it)
        :return: list of coordinates around previous coordinate of path that are still unused in current path
        """
        if not self.__list_of_cords:
            # if the path is empty, every coordinate is possible, return "All" as flag
            return "All"
        current_row, current_col = self.__list_of_cords[-1]
        valid_moves = []
        possible_moves = [(current_row+1, current_col), (current_row-1, current_col),
                          (current_row, current_col+1), (current_row, current_col-1),
                          (current_row+1, current_col-1), (current_row+1, current_col+1),
                          (current_row-1, current_col-1), (current_row-1, current_col+1)]
        # make sure the coordinate has not yet been used in path and that it is not a negative value:
        for move in possible_moves:
            if move not in self.__list_of_cords:
                if move[0] >= 0 and move[1] >= 0:
                    valid_moves.append(move)
        return valid_moves

    def add_cord(self, coordinate: Tuple[int, int]) -> bool:
        """
        adds a coordinate to the path if possible
        :param coordinate: a coordinate to be added to path
        :return: whether the coordinate was added or not - boolean value
        """
        if self.possible_moves() == "All" or coordinate in self.possible_moves():
            # if the addition of the coordinate is possible than add it to path, update the length, and return True
            self.__length += 1
            self.__list_of_cords.append(coordinate)
            return True
        return False

    def remove_last(self) -> Optional[Tuple[int, int]]:
        """
        removes last coordinate of the path
        :return: the coordinate removed (unless the path was empty)
        """
        if not self.__list_of_cords:
            return
        # if the path is not empty, update the length, and remove and return the last coordinate of path
        self.__length -= 1
        return self.__list_of_cords.pop()
