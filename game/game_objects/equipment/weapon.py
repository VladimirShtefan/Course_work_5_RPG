from dataclasses import dataclass
from random import uniform


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self) -> float:
        hit = uniform(self.min_damage, self.max_damage)
        return hit
