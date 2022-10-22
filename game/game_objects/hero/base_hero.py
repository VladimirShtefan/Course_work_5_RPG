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

    def check_stamina_for_attack(self) -> bool:
        return self.weapon.check_enough_stamina(self.unit_class.stamina)

    def attack(self, defensive_block: float) -> float:
        max_damage: float = self.weapon.damage * self.unit_class.attack
        damage: float = max(max_damage - defensive_block, 0.0)
        self.__reduce_health(damage)
        return damage

    def block(self) -> float:
        if self.armor.check_enough_stamina(self.unit_class.stamina):
            return self.armor.defence * self.unit_class.armor
        return 0.0

    def __reduce_health(self, damage: float) -> None:
        self.unit_class.max_health -= damage


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
