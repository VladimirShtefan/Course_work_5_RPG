from flask import Flask

from game.user_interface.flask.blueprints.choose_blueprint.views import choose_blueprint
from game.user_interface.flask.blueprints.game_blueprint.views import game_blueprint
from game.user_interface.flask.blueprints.index_blueprint.views import index_blueprint


def init_app(config) -> Flask:
    flask_app: Flask = Flask(__name__)
    flask_app.config.from_object(config)
    register_blueprints(flask_app)
    return flask_app


def register_blueprints(flask_app: Flask) -> None:
    flask_app.register_blueprint(index_blueprint)
    flask_app.register_blueprint(choose_blueprint)
    flask_app.register_blueprint(game_blueprint)





