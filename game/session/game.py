import hashlib

from game.session.user import User


class Game(object):
    __users = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def __get_player_id(remote_addr: str, user_info: dict) -> str:
        player_hash = hashlib.md5(''.join([remote_addr,
                                           user_info['User-Agent']]
                                          ).encode())
        player_id: str = player_hash.hexdigest()
        return player_id

    def __search_player(self, player_id: str) -> dict | None:
        if player_id in self.__users:
            return self.__users[player_id]

    def get_player(self, remote_addr: str, user_info: dict) -> User:
        player_id: str = self.__get_player_id(remote_addr, user_info)
        if not self.__search_player(player_id):
            self.__users[player_id] = User(player_id)
        return self.__users[player_id]
