from dataclasses import dataclass

from game.game_objects.hero.skills import Skill, Warrior_ult, Thief_ult, Archer_ult


@dataclass
class Specialization:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


Warrior = Specialization(name='Воин',
                         max_health=60.0,
                         max_stamina=30.0,
                         attack=0.8,
                         stamina=2.0,
                         armor=1.2,
                         skill=Warrior_ult)

Thief = Specialization(name='Вор',
                       max_health=50.0,
                       max_stamina=25.0,
                       attack=1.5,
                       stamina=1.2,
                       armor=1.0,
                       skill=Thief_ult)

Archer = Specialization(name='Лучник',
                        max_health=40.0,
                        max_stamina=20.0,
                        attack=1.9,
                        stamina=1.5,
                        armor=0.6,
                        skill=Archer_ult)

SPECS = (Warrior, Thief, Archer)
