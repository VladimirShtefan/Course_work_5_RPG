from game.game_objects.hero.hero import Character


class BattleStatistic:
    def __init__(self, attacking: Character, defensive: Character):
        self.__attacking: Character = attacking
        self.__defensive: Character = defensive

    def print_log_attacking(self, damage=None):
        if damage is None:
            return f' {self.__attacking.name}, попытался использовать {self.__attacking.weapon.name}, ' \
                   f'но у него не хватило выносливости.'
        if damage > 0.0:
            return f' {self.__attacking.name}, используя {self.__attacking.weapon.name}, ' \
                   f'пробивает {self.__defensive.armor.name} соперника и наносит {damage} урона.'
        return f' {self.__attacking.name}, используя {self.__attacking.weapon.name}, ' \
               f'наносит удар, но {self.__defensive.armor.name} соперника его останавливает.'

    def print_log_die(self, attacking: bool, defensive: bool):
        if attacking:
            return f' {self.__defensive.name} выиграл битву.'
        elif defensive:
            return f' {self.__attacking.name} выиграл битву.'

    def print_log_ult(self, damage=None):
        if damage is None:
            return f' {self.__attacking.name}, попытался использовать {self.__attacking.unit_class.skill.name}, ' \
                   f'но у него не хватило выносливости.'
        if damage > 0.0:
            return f' {self.__attacking.name}, использует {self.__attacking.unit_class.skill.name}, ' \
                   f'и наносит {damage} урона сопернику.'
        else:
            return f' {self.__attacking.name} уже использовал навык.'

    def print_skip_log(self):
        return f' {self.__defensive.name}, пропускает ход.'
