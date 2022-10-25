from dataclasses import dataclass, field

from constants import RECOVERY_STAMINA_PER_TURN
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
    stamina_points: float = field(default=0.0)
    health_points: float = field(default=0.0)

    def set_name(self, name: str) -> None:
        self.name = name

    def set_unit_class(self, unit_class: str) -> None:
        for spec in SPECS:
            if spec.name == unit_class:
                self.unit_class = spec
                self.stamina_points = spec.max_stamina
                self.health_points = spec.max_health
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
            self.stamina_points = round(self.stamina_points - self.weapon.stamina_per_hit, 2)
            return True

    def attack(self, defensive_block: float) -> float:
        max_damage: float = round(self.weapon.damage * self.unit_class.attack, 2)
        damage: float = round(max(max_damage - defensive_block, 0.0), 2)
        self.__recovery_stamina()
        return damage

    def check_stamina_for_ult(self) -> bool:
        return self.stamina_points > self.unit_class.skill.cost

    def use_ult(self) -> float:
        if not self.unit_class.skill.used:
            self.unit_class.skill.used = True
            self.stamina_points = round(self.stamina_points - self.unit_class.skill.cost, 2)
            return self.unit_class.skill.damage
        return 0.0

    def block(self) -> float:
        if self.stamina_points > self.armor.stamina_per_turn:
            return self.armor.defence * self.unit_class.armor
        self.__recovery_stamina()
        return 0.0

    def __recovery_stamina(self) -> None:
        recovery_stamina = round(self.stamina_points + RECOVERY_STAMINA_PER_TURN * self.unit_class.stamina, 2)
        if recovery_stamina > self.unit_class.max_stamina:
            self.stamina_points = self.unit_class.max_stamina
        else:
            self.stamina_points = recovery_stamina

    def reduce_health(self, damage: float) -> None:
        health = round(self.health_points - damage, 2)
        if health < 0.0:
            self.health_points = 0.0
        else:
            self.health_points = health

    def check_die(self) -> True:
        if self.health_points == 0:
            return True


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
