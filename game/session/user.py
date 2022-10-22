from game.game_objects.hero.base_hero import Character
from game.session.battle_statistics import BattleStatistic
from game.session.controller import Controller


class User:
    def __init__(self) -> None:
        self.__position: Controller = Controller()
        self.__character: Character | None = None
        self.__enemy_character: Character | None = None

    @property
    def character(self) -> Character:
        return self.__character

    @property
    def enemy_character(self) -> Character:
        return self.__enemy_character

    def get_status(self) -> str:
        return self.__position.position_in_game

    def delete_start_position(self) -> None:
        self.__position.delete_start_position()

    def set_next_queue(self) -> str:
        return self.__position.set_next_queue()

    def set_user_character(self, character: Character) -> None:
        self.__character: Character = character

    def set_enemy_for_user(self, character: Character) -> None:
        self.__enemy_character: Character = character

    def hit(self) -> list[str]:
        attacking: Character = self.__character
        defensive: Character = self.__enemy_character
        result_battle = []
        for _ in range(2):
            battle = BattleStatistic(attacking=attacking, defensive=defensive)
            if attacking.check_stamina_for_attack():
                block = defensive.block()
                max_damage, damage = attacking.attack(block)
                result_battle.append(battle.print_log_attacking(max_damage, damage, block))
                attacking, defensive = defensive, attacking
            else:
                result_battle.append(battle.print_log_attacking())
                attacking, defensive = defensive, attacking
                continue
        return result_battle

