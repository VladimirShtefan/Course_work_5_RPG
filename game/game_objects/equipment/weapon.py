from dataclasses import dataclass


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float


    # @property
    # def damage(self):
    #     pass
