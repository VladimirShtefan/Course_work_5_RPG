import json
from dataclasses import dataclass

import marshmallow
import marshmallow_dataclass

from constants import EQUIPMENT_JSON
from game.game_objects.equipment.armor import Armor
from game.game_objects.equipment.weapon import Weapon


@dataclass
class Equipment:
    weapons: list[Weapon]
    armors: list[Armor]


class EquipmentItems:
    def __init__(self):
        self.__equipment = self.__get_equipment_data()

    @property
    def equipment(self):
        return self.__equipment

    @staticmethod
    def __get_equipment_data():
        with open(EQUIPMENT_JSON, 'r', encoding='utf-8') as file:
            equipment = json.load(file)
        equipment_schema = marshmallow_dataclass.class_schema(Equipment)
        try:
            return equipment_schema().load(equipment)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
