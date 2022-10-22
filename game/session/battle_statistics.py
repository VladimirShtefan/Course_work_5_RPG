from game.game_objects.hero.base_hero import Character


class BattleStatistic:
    def __init__(self, attacking: Character, defensive: Character):
        self.__attacking: Character = attacking
        self.__defensive: Character = defensive

    def print_log_attacking(self, damage=None, block=None):
        print(damage)
        print(block)
        if damage is None:
            return f'{self.__attacking.name}, попытался использовать {self.__attacking.weapon.name}, ' \
                   f'но у него не хватило выносливости.'
        if damage > block:
            return f'{self.__attacking.name}, используя {self.__attacking.weapon.name}, ' \
                   f'пробивает {self.__defensive.armor.name} соперника и наносит {damage} урона'
        return f'{self.__attacking.name}, используя {self.__attacking.weapon.name}, ' \
               f'наносит удар, но {self.__defensive.armor.name} соперника его останавливает'
