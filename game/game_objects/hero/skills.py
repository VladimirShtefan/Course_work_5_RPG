from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    damage: float
    cost: float


Warrior_ult = Skill(name='Свирепый пинок', damage=12.0, cost=6.0)
Thief_ult = Skill(name='Мощный укол', damage=15.0, cost=5.0)
Archer_ult = Skill(name='Дождь стрел', damage=18.0, cost=3.5)
