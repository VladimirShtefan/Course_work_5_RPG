from game.game_objects.hero.hero import Character
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
        result_battle: list = []
        for _ in range(2):
            battle: BattleStatistic = BattleStatistic(attacking=attacking, defensive=defensive)
            if defensive.check_die() or attacking.check_die():
                result_battle.append(
                    battle.print_log_die(attacking=attacking.check_die(), defensive=defensive.check_die()))
                break
            if attacking.check_stamina_for_attack():
                block: float = defensive.block()
                damage: float = attacking.attack(block)
                defensive.reduce_health(damage)
                result_battle.append(battle.print_log_attacking(damage))
                attacking, defensive = defensive, attacking
            else:
                result_battle.append(battle.print_log_attacking())
                attacking, defensive = defensive, attacking
        return result_battle

    def ult(self) -> list[str]:
        attacking: Character = self.__character
        defensive: Character = self.__enemy_character
        result_battle: list = []
        for _ in range(2):
            battle: BattleStatistic = BattleStatistic(attacking=attacking, defensive=defensive)
            if defensive.check_die() or attacking.check_die():
                result_battle.append(
                    battle.print_log_die(attacking=attacking.check_die(), defensive=defensive.check_die()))
                break
            if attacking.check_stamina_for_ult():
                damage: float = attacking.use_ult()
                defensive.reduce_health(damage)
                result_battle.append(battle.print_log_ult(damage))
                attacking, defensive = defensive, attacking
            else:
                result_battle.append(battle.print_log_ult())
                attacking, defensive = defensive, attacking
        return result_battle

    def pass_turn(self) -> list[str]:
        attacking: Character = self.__enemy_character
        defensive: Character = self.__character
        result_battle: list = []
        battle: BattleStatistic = BattleStatistic(attacking=attacking, defensive=defensive)
        if defensive.check_die() or attacking.check_die():
            result_battle.append(
                battle.print_log_die(attacking=attacking.check_die(), defensive=defensive.check_die()))
            return result_battle
        result_battle.append(battle.print_skip_log())
        if attacking.check_stamina_for_attack():
            block: float = defensive.block()
            damage: float = attacking.attack(block)
            defensive.reduce_health(damage)
            result_battle.append(battle.print_log_attacking(damage))
            if defensive.check_die():
                result_battle.append(
                    battle.print_log_die(attacking=attacking.check_die(), defensive=defensive.check_die()))
        else:
            result_battle.append(battle.print_log_attacking())
        return result_battle

    def end_fight(self) -> None:
        self.__position.set_next_queue()
