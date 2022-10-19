from flask import Flask, render_template, request, redirect

from game.game_objects.equipment.equipment import EquipmentItems
from game.game_objects.hero.base_hero import HeroBuilder
from game.game_objects.hero.specialization import SPECS
from game.session.game import Game
from game.user_interface.flask.config import DevConfig, ProdConfig
from game.session.user import User


def init_app() -> Flask:
    flask_app = Flask(__name__)

    with flask_app.app_context():
        match flask_app.config.get('ENV'):
            case 'development':
                flask_app.config.from_object(DevConfig)
            case 'production':
                flask_app.config.from_object(ProdConfig)
            case _:
                raise RuntimeError('Need to set environment variable FLASK_ENV')
        return flask_app


app = init_app()


@app.get('/')
def index():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if request.path == '/' and status == '/':
        return render_template('index.html')
    return redirect(status)


@app.get('/choose-hero/')
def choose_hero():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    user.start_game()
    if status != '/choose-hero/':
        return redirect(status)
    equipment = EquipmentItems().equipment
    return render_template('hero_choosing.html', result={'classes': (spec.name for spec in SPECS),
                                                         'weapons': (weapon.name for weapon in equipment.weapons),
                                                         'armors': (armor.name for armor in equipment.armors)
                                                         })


@app.post('/choose-hero/')
def create_hero():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    character = HeroBuilder(**request.form).hero
    user.set_user_character(character)
    if status == '/choose-hero/':
        status = user.set_next_queue()
        return redirect(status)
    return redirect(status)


@app.get('/choose-enemy/')
def choose_enemy():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status == '/choose-enemy/':
        return render_template('choosing_enemy.html')
    return redirect(status)


@app.post('/choose-enemy/')
def get_enemy():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status == '/choose-enemy/':
        return redirect('/search_enemy/')
    return redirect(status)


@app.get('/search_enemy/')
def search_enemy():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status == '/choose-enemy/':
        return 'поиск'
        # return render_template('choosing_enemy.html')
    return redirect(status)


@app.get('/fight/')
def fight():
    user: User = Game().get_player(remote_addr=request.remote_addr, user_info=request.headers)
    status: str = user.get_status()
    if status != '/fight/':
        return redirect(status)
    return render_template('fight.html', result={'classes': ['1', '2', '3'],
                                                 'weapons': ['1', '2', '3'],
                                                 'armors': ['1', '2', '3']})
