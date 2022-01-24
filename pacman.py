import enum
import os
import random
import time
import msvcrt

key_input = ''
score = 0
class GType(enum.Enum):
    default = -1
    pacman = 0
    ghost = 1
    wall = 2
    dot = 3

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

class GameObj:
    type = GType.default
    position = (0, 0)
    direction = (0, 0)
    sprite = '*'

    def __init__(self, position, direction, sprite, gtype):
        self.position = position
        self.direction = direction
        self.sprite = sprite
        self.type = gtype

default = GameObj((0, 0), (0, 0), '\u2591', GType.default)
pacman = GameObj((1, 18), (0, -1), 'e', GType.pacman)
walls = list()
ghosts = list()
dots = list()

for i in range(0, 20):
    walls.append(GameObj((0, i), (0, 0), '\u2588', GType.wall))
    walls.append(GameObj((i, 0), (0, 0), '\u2588', GType.wall))
    walls.append(GameObj((19, i), (0, 0), '\u2588', GType.wall))
    walls.append(GameObj((i, 19), (0, 0), '\u2588', GType.wall))

for i in range(2, 18):
    if i != 5 and i != 10 and i != 14:
        walls.append(GameObj((2, i), (0, 0), '\u2588', GType.wall))
    if i != 5 and i != 10 and i != 15:
        walls.append(GameObj((i, 2), (0, 0), '\u2588', GType.wall))
    if i != 5 and i != 9 and i != 14:
        walls.append(GameObj((17, i), (0, 0), '\u2588', GType.wall))
    if i != 5 and i != 10 and i != 15:
        walls.append(GameObj((i, 17), (0, 0), '\u2588', GType.wall))

for i in range(4, 16):
    if i != 10:
        walls.append(GameObj((4, i), (0, 0), '\u2588', GType.wall))
    if i != 6 and i != 13:
        walls.append(GameObj((i, 4), (0, 0), '\u2588', GType.wall))
    if i != 9:
        walls.append(GameObj((15, i), (0, 0), '\u2588', GType.wall))
    if i != 7 and i != 13:
        walls.append(GameObj((i, 15), (0, 0), '\u2588', GType.wall))

for i in range(6, 14):
    if i != 10:
        walls.append(GameObj((6, i), (0, 0), '\u2588', GType.wall))
    if i != 10:
        walls.append(GameObj((i, 6), (0, 0), '\u2588', GType.wall))
    if i != 9:
        walls.append(GameObj((13, i), (0, 0), '\u2588', GType.wall))
    if i != 9:
        walls.append(GameObj((i, 13), (0, 0), '\u2588', GType.wall))

for i in range(8, 12):
    walls.append(GameObj((8, i), (0, 0), '\u2588', GType.wall))
    if i != 10:
        walls.append(GameObj((i, 8), (0, 0), '\u2588', GType.wall))
    walls.append(GameObj((11, i), (0, 0), '\u2588', GType.wall))
    if i != 9:
        walls.append(GameObj((i, 11), (0, 0), '\u2588', GType.wall))

ghosts.append(GameObj((18, 1), (-1, 0), "@", GType.ghost))
ghosts.append(GameObj((18, 18), (0, -1), "@", GType.ghost))
ghosts.append(GameObj((1, 1), (1, 0), "@", GType.ghost))
ghosts.append(GameObj((5, 14), (-1, 0), "@", GType.ghost))

for i in range(1, 19):
    dots.append(GameObj((1, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 1), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((18, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 18), (0, 0), '\u00B0', GType.dot))

for i in range(3, 17):
    dots.append(GameObj((3, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 3), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((16, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 16), (0, 0), '\u00B0', GType.dot))

for i in range(5, 15):
    dots.append(GameObj((5, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 5), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((14, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 14), (0, 0), '\u00B0', GType.dot))

for i in range(7, 13):
    dots.append(GameObj((7, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 7), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((12, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 12), (0, 0), '\u00B0', GType.dot))

for i in range(9, 11):
    dots.append(GameObj((9, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 9), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((10, i), (0, 0), '\u00B0', GType.dot))
    dots.append(GameObj((i, 10), (0, 0), '\u00B0', GType.dot))

world = [[list() for i in range(20)] for j in range(20)]

def world_generate():
    global world
    world = [[list() for i in range(20)] for j in range(20)]
    world[pacman.position[0]][pacman.position[1]].append(pacman)

    for o in ghosts:
        world[o.position[0]][o.position[1]].append(o)

    for o in walls:
        world[o.position[0]][o.position[1]].append(o)

    for o in dots:
        world[o.position[0]][o.position[1]].append(o)

    for i in range(0, 20):
        for j in range(0, 20):
            world[i][j].append(default)

def world_print():
    for i in range(20):
        for j in range(20):
            print(world[i][j][0].sprite, end='')
        print()
    print("Score = {0}".format(score))

def state_update():
    global score
    for o in ghosts:
        flag = False
        for ow in world[o.position[0]+o.direction[0]][o.position[1]+o.direction[1]]:
            if ow.type == GType.wall:
                flag = True
        while flag or o.direction[0] == o.direction[1] or o.direction[0]+o.direction[1] == 0:
            o.direction = (random.randrange(-1, 2), random.randrange(-1, 2))
            for ow in world[o.position[0]+o.direction[0]][o.position[1]+o.direction[1]]:
                if ow.type == GType.wall:
                    flag = True
                    break
                else:
                    flag = False
        o.position = (o.position[0] + o.direction[0], o.position[1] + o.direction[1])

    c = 0
    for o in world[pacman.position[0]][pacman.position[1]]:
        if o.type == GType.ghost:
            return False
        if o.type == GType.dot:
            dots.remove(o)
            score = score+1
        c = c + 1

    if key_input == 'w' and world[pacman.position[0]-1][pacman.position[1]][0].type != GType.wall:
        pacman.direction = (-1, 0)
    elif key_input == 's' and world[pacman.position[0]+1][pacman.position[1]][0].type != GType.wall:
        pacman.direction = (1, 0)
    elif key_input == 'd' and world[pacman.position[0]][pacman.position[1]+1][0].type != GType.wall:
        pacman.direction = (0, 1)
    elif key_input == 'a' and world[pacman.position[0]][pacman.position[1]-1][0].type != GType.wall:
        pacman.direction = (0, -1)

    if world[pacman.position[0]+pacman.direction[0]][pacman.position[1]+pacman.direction[1]][0].type == GType.wall:
        pacman.direction = (0, 0)
    else:
        pacman.position = (pacman.position[0] + pacman.direction[0], pacman.position[1] + pacman.direction[1])


if __name__ == '__main__':
    win = False
    world_generate()
    world_print()
    while True:

        if msvcrt.kbhit():
            key_input = msvcrt.getch().decode('utf-8')

        clearConsole()

        if state_update() == False:
            break
        if not dots:
            win = True
            break
        world_generate()
        world_print()

        time.sleep(0.1)
    if win:
        print("HooooooooooooooooRAAAYYYyyy!!")
    else:
        print("LoooooSerrrrr!!!")
#loop
#input
#state
#print