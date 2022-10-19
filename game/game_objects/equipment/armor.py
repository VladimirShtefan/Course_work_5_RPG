from dataclasses import dataclass


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float
