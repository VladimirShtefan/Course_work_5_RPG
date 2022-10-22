from dataclasses import dataclass


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float

    def check_enough_stamina(self, current_stamina: float) -> bool:
        return current_stamina > self.stamina_per_turn
