import os

from game.user_interface.flask.config import DevConfig, ProdConfig
from game.user_interface.flask.flask_app import init_app


if os.environ.get('FLASK_DEBUG'):
    app = init_app(DevConfig)
else:
    app = init_app(ProdConfig)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
