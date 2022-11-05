import hashlib

from game.session.user import User


class Game(object):
    __instance = None
    __players: dict = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.__instance = super(Game, cls).__new__(cls)
        return cls.__instance

    @staticmethod
    def __get_player_id(remote_addr: str, user_info: dict) -> str:
        player_hash = hashlib.md5(''.join([remote_addr,
                                           user_info['User-Agent']]
                                          ).encode())
        player_id: str = player_hash.hexdigest()
        return player_id

    def __search_player(self, player_id: str) -> dict | None:
        if player_id in self.__players:
            return self.__players[player_id]

    def get_player(self, remote_addr: str, user_info: dict) -> User:
        player_id: str = self.__get_player_id(remote_addr, user_info)
        if not self.__search_player(player_id):
            self.__players[player_id]: User = User()
        return self.__players[player_id]
