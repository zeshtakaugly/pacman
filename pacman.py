import enum


class GType(enum.Enum):
    default = -1
    pacman = 0
    ghost = 1
    wall = 2
    dot = 3


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

world = [['\u2591' for i in range(20)] for j in range(20)]

def world_generate():
    for o in walls:
        world[o.position[1]][o.position[0]] = o.sprite

    for o in ghosts:
        world[o.position[1]][o.position[0]] = o.sprite

def world_print():
    for i in range(20):
        for j in range(20):
            print(world[i][j], end='')
        print()

#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

#loop
    #input
    #state
    #print