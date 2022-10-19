from constants import QUEUE


class Controller:
    def __init__(self) -> None:
        self.__queue = QUEUE

    @property
    def status_game(self) -> str:
        return self.__get_status_game()

    def start_game(self) -> None:
        if '/' in self.__queue:
            self.__queue.remove('/')

    def set_next_queue(self) -> str:
        return self.__queue.pop(0)

    def __get_status_game(self) -> str:
        if self.__queue:
            return self.__queue[0]
        return self.__reset_queue()

    def __reset_queue(self) -> str:
        self.__queue = QUEUE
        return self.__queue[0]
