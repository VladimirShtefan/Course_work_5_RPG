from flask import request, render_template, redirect, Blueprint, jsonify
from flask_cors import CORS

from exceptions import DataError
from game.game_objects.equipment.equipment import EquipmentItems, Equipment
from game.game_objects.hero.hero import HeroBuilder, Character
from game.game_objects.hero.specialization import SPECS
from game.session.game import Game
from game.session.user import User
from game.user_interface.flask.path_file import TEMPLATES_PATH


choose_blueprint = Blueprint('choose_blueprint', __name__, template_folder=TEMPLATES_PATH)

CORS(choose_blueprint, origins=['http://vshtefan.ga', 'http://127.0.0.1'])


@choose_blueprint.get('/choose-hero/')
def choose_hero():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    user.delete_start_position()
    if status != '/choose-hero/':
        return redirect(status)
    try:
        equipment: Equipment = EquipmentItems().equipment
    except DataError as e:
        return jsonify({'Код ошибки': e.code,
                        'Сообщение': f'{e.message}'})
    return render_template('hero_choosing.html', result={'header': 'Выберите класс и экипировку',
                                                         'classes': (spec.name for spec in SPECS),
                                                         'weapons': (weapon.name for weapon in equipment.weapons),
                                                         'armors': (armor.name for armor in equipment.armors)
                                                         })


@choose_blueprint.post('/choose-hero/')
def create_hero():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status == '/choose-hero/':
        character: Character = HeroBuilder(**request.form).hero
        user.set_user_character(character)
        status: str = user.set_next_queue()
        return redirect(status)
    return redirect(status)


@choose_blueprint.get('/choose-enemy/')
def choose_enemy():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/choose-enemy/':
        return redirect(status)
    try:
        equipment: Equipment = EquipmentItems().equipment
    except DataError as e:
        return jsonify({'Код ошибки': e.code,
                        'Сообщение': f'{e.message}'})
    return render_template('hero_choosing.html', result={'header': 'Выберите класс и экипировку для противника',
                                                         'classes': (spec.name for spec in SPECS),
                                                         'weapons': (weapon.name for weapon in equipment.weapons),
                                                         'armors': (armor.name for armor in equipment.armors)
                                                         })


@choose_blueprint.post('/choose-enemy/')
def get_enemy():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status == '/choose-enemy/':
        character: Character = HeroBuilder(**request.form).hero
        user.set_enemy_for_user(character)
        status: str = user.set_next_queue()
        return redirect(status)
    return redirect(status)

