from pathlib import Path


FLASK_PATH = Path(__file__).parent
TEMPLATES_PATH = Path.joinpath(FLASK_PATH, 'blueprints', 'static', 'templates')
