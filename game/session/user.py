#
# class Data:
#     def __init__(self):
#         self.path = USERS_JSON
#
#     def load_users(self) -> dict:
#         with open(self.path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return data
#
#     def write_user(self, data: dict):
#         with open(self.path, 'w', encoding='utf-8') as file:
#             json.dump(data, file, indent=4, ensure_ascii=False)
from game.game_objects.hero.base_hero import Character
from game.session.controller import Controller


class User:
    def __init__(self, player_id) -> None:
        self.__game = Controller()
        self.__player_id = player_id
        self.__character = None

    @property
    def character(self):
        return self.__character

    def get_status(self) -> str:
        return self.__game.status_game

    def start_game(self):
        self.__game.start_game()

    def set_next_queue(self) -> str:
        return self.__game.set_next_queue()

    def set_user_character(self, character: Character):
        self.__character = character
