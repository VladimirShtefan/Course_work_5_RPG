from flask import request, render_template, redirect, Blueprint
from flask_cors import CORS

from game.session.game import Game
from game.session.user import User
from game.user_interface.flask.path_file import TEMPLATES_PATH


index_blueprint = Blueprint('index_blueprint', __name__, template_folder=TEMPLATES_PATH)

CORS(index_blueprint, origins=['http://vshtefan.ga', 'http://127.0.0.1'])


@index_blueprint.get('/')
def index():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if request.path == '/' and status == '/':
        return render_template('index.html')
    return redirect(status)
