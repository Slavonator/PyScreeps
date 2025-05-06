from map_related_files.game_map import *
from map_related_files.map_generator import *
from map_related_files.resources import *
from map_related_files.tiles import *
import numpy as np


def show_map(map):

    for row in map:
        for index in row:
            print(MAP_TILES[index](), end='')
        print()


map = np.zeros((64, 64), dtype=int)

show_map(map)