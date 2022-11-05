from flask import request, render_template, redirect, Blueprint

from game.game_objects.hero.hero import Character
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
    result: str = 'Бой начался'
    battle_result: str = ''
    return render_template('fight.html', heroes=heroes, result=result, battle_result=battle_result)


@game_blueprint.get('/hit/')
def hit():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/fight/':
        return redirect(status)
    result: list[str] = user.hit()
    heroes: dict[str, Character] = {'player': user.character,
                                    'enemy': user.enemy_character}
    return render_template('fight.html', heroes=heroes, result='', battle_result=''.join(result))


@game_blueprint.get('/use-skill/')
def use_skill():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/fight/':
        return redirect(status)
    result: list[str] = user.ult()
    heroes: dict[str, Character] = {'player': user.character,
                                    'enemy': user.enemy_character}
    return render_template('fight.html', heroes=heroes, result='', battle_result=''.join(result))


@game_blueprint.get('/pass-turn/')
def pass_turn():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/fight/':
        return redirect(status)
    result: list[str] = user.pass_turn()
    heroes: dict[str, Character] = {'player': user.character,
                                    'enemy': user.enemy_character}
    return render_template('fight.html', heroes=heroes, result='', battle_result=''.join(result))


@game_blueprint.get('/end-fight/')
def end_fight():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/fight/':
        return redirect(status)
    user.end_fight()
    status: str = user.get_status()
    return redirect(status)
