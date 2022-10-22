from flask import request, render_template, redirect, Blueprint

from game.session.game import Game
from game.session.user import User
from game.user_interface.flask.path_file import TEMPLATES_PATH


game_blueprint = Blueprint('game_blueprint', __name__, template_folder=TEMPLATES_PATH, url_prefix='/fight/')


@game_blueprint.get('/')
def fight():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/fight/':
        return redirect(status)
    heroes = {'player': user.character,
              'enemy': user.enemy_character}
    result = 'Бой начался'
    battle_result = ''
    return render_template('fight.html', heroes=heroes, result=result, battle_result=battle_result)


@game_blueprint.get('/hit/')
def hit():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/fight/':
        return redirect(status)
    result = user.hit()
    heroes = {'player': user.character,
              'enemy': user.enemy_character}
    return render_template('fight.html', heroes=heroes, result='', battle_result=''.join(result))
