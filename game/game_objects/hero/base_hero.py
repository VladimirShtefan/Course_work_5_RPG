from decimal import Decimal, getcontext
from dataclasses import dataclass, field

from game.game_objects.equipment.armor import Armor
from game.game_objects.equipment.equipment import EquipmentItems
from game.game_objects.equipment.weapon import Weapon
from game.game_objects.hero.specialization import Specialization, SPECS


getcontext().prec = 1


@dataclass
class Character:
    name: str = field(default=None)
    unit_class: Specialization = field(default=None)
    weapon: Weapon = field(default=None)
    armor: Armor = field(default=None)
    stamina_points: Decimal = field(default=0.0)
    health_points: Decimal = field(default=Decimal(0.0))

    def set_name(self, name: str) -> None:
        self.name = name

    def set_unit_class(self, unit_class: str) -> None:
        for spec in SPECS:
            if spec.name == unit_class:
                self.unit_class = spec
                self.stamina_points = Decimal(spec.max_stamina)
                self.health_points = Decimal(spec.max_health)
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
        if self.stamina_points > self.weapon.stamina_per_hit:
            self.stamina_points -= Decimal(self.weapon.stamina_per_hit)
            return True

    def attack(self, defensive_block: Decimal) -> tuple[Decimal, Decimal]:
        max_damage: Decimal = Decimal(self.weapon.damage * self.unit_class.attack)
        damage: Decimal = Decimal(max(max_damage - defensive_block, Decimal(0.0)))
        self.__reduce_health(damage)
        return max_damage, damage

    def block(self) -> Decimal:
        if self.stamina_points > self.armor.stamina_per_turn:
            return Decimal(self.armor.defence * self.unit_class.armor)
        return Decimal(0.0)

    def __reduce_health(self, damage: Decimal) -> None:
        self.health_points -= damage


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
