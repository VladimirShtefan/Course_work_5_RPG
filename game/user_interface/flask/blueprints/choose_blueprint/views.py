from flask import request, render_template, redirect, Blueprint

from game.game_objects.equipment.equipment import EquipmentItems
from game.game_objects.hero.base_hero import HeroBuilder
from game.game_objects.hero.specialization import SPECS
from game.session.game import Game
from game.session.user import User
from game.user_interface.flask.path_file import TEMPLATES_PATH


choose_blueprint = Blueprint('choose_blueprint', __name__, template_folder=TEMPLATES_PATH)


@choose_blueprint.get('/choose-hero/')
def choose_hero():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    user.delete_start_position()
    if status != '/choose-hero/':
        return redirect(status)
    equipment = EquipmentItems().equipment
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
        character = HeroBuilder(**request.form).hero
        user.set_user_character(character)
        status = user.set_next_queue()
        return redirect(status)
    return redirect(status)


@choose_blueprint.get('/choose-enemy/')
def choose_enemy():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/choose-enemy/':
        return redirect(status)
    equipment = EquipmentItems().equipment
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
        character = HeroBuilder(**request.form).hero
        user.set_enemy_for_user(character)
        status = user.set_next_queue()
        return redirect(status)
    return redirect(status)

