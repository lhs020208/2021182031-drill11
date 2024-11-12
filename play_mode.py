import random

from pico2d import *

import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global balls
    global zombies

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    balls = [Ball(random.randint(0,800),60,0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    game_world.add_collision_pair('boy:ball',boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball',None, ball)

    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)


    game_world.add_collision_pair('boy:zombie', boy, None)
    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie', None, zombie)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

    for ball in game_world.world[0]:
        # is_removed가 True인 Ball은 제외
        if isinstance(ball, Ball) and not ball.is_removed and ball.velocity != 0:
            game_world.add_collision_pair('zombie:ball', ball, None)
            for zombie in zombies:
                if not zombie.is_removed :
                    game_world.add_collision_pair('zombie:ball', None, zombie)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

