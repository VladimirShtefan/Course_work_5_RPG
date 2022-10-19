from dataclasses import dataclass, field

from game.game_objects.equipment.armor import Armor
from game.game_objects.equipment.equipment import EquipmentItems
from game.game_objects.equipment.weapon import Weapon
from game.game_objects.hero.specialization import Specialization, SPECS


@dataclass
class Character:
    name: str = field(default=None)
    unit_class: Specialization = field(default=None)
    weapon: Weapon = field(default=None)
    armor: Armor = field(default=None)

    def set_name(self, name: str) -> None:
        self.name = name

    def set_unit_class(self, unit_class: str) -> None:
        for spec in SPECS:
            if spec.name == unit_class:
                self.unit_class = spec
                return

    def set_weapon(self, weapon: str) -> None:
        weapons = EquipmentItems().equipment.weapons
        for _weapon in weapons:
            if _weapon.name == weapon:
                self.weapon = _weapon
                return

    def set_hero_armor(self, armor: str) -> None:
        armors = EquipmentItems().equipment.armors
        for _armor in armors:
            if _armor.name == armor:
                self.armor = _armor
                return


class HeroBuilder:
    def __init__(self, name, unit_class, weapon, armor):
        self.__name = name
        self.__unit_class = unit_class
        self.__weapon = weapon
        self.__armor = armor

    def __reset(self):
        self.__hero: Character = Character()

    @property
    def hero(self) -> Character:
        self.__reset()
        self.__hero.set_name(self.__name)
        self.__hero.set_unit_class(self.__unit_class)
        self.__hero.set_weapon(self.__weapon)
        self.__hero.set_hero_armor(self.__armor)
        return self.__hero


#
# class Builder(ABC):
#     @property
#     @abstractmethod
#     def hero(self) -> None:
#         pass

    # @abstractmethod
    # def set_hero_name(self, name: str) -> None:
    #     pass
    #
    # @abstractmethod
    # def set_hero_class(self, hero_class: str) -> None:
    #     pass
    #
    # @abstractmethod
    # def set_hero_weapon(self, weapon: str) -> None:
    #     pass
    #
    # @abstractmethod
    # def set_hero_armor(self, armor: str) -> None:
    #     pass




    # def set_hero_name(self, name) -> None:
    #     self.__hero.name = name
    #
    # def set_hero_class(self, hero_class: str) -> None:
    #     print(hero_class)
    #     self.__hero.unit_class = [spec for spec in SPECS if spec.name == hero_class]
    #
    # def set_hero_weapon(self, weapon: str) -> None:
    #     print(weapon)
    #     weapons = EquipmentItems().equipment.weapons
    #     self.__hero.weapon = [weapon for weapon in weapons if weapon.name == weapon]
    #
    # def set_hero_armor(self, armor: str) -> None:
    #     print(armor)
    #     armors = EquipmentItems().equipment.armors
    #     self.__hero.armor = [armor for armor in armors if armor.name == armor]
