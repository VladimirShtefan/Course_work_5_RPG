from pathlib import Path


ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
EQUIPMENT_JSON = Path.joinpath(DATA_PATH, 'equipment.json')
USERS_JSON = Path.joinpath(DATA_PATH, 'users.json')


QUEUE: list[str] = ['/', '/choose-hero/', '/choose-enemy/', '/fight/']

RECOVERY_STAMINA_PER_TURN: float = 1.0
