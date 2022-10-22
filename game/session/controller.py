from constants import QUEUE


class Controller:
    def __init__(self) -> None:
        self.__queue = QUEUE[:]

    @property
    def position_in_game(self) -> str:
        return self.__get_position()

    def delete_start_position(self) -> None:
        if '/' in self.__queue:
            self.__queue.remove('/')

    def set_next_queue(self) -> str:
        return self.__queue.pop(0)

    def __get_position(self) -> str:
        if self.__queue:
            return self.__queue[0]
        return self.__reset_queue()

    def __reset_queue(self) -> str:
        self.__queue = QUEUE[:]
        return self.__queue[0]
