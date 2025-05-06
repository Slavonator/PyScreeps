from map_related_files.map_generator import *
from map_related_files.resources import *
from map_related_files.tiles import *
import numpy as np


def convert_numbermap_to_map(map):

    for x in range(64):
        for y in range(64):
            map[x][y] = MAP_TILES[map[x][y]]


def show_map(map):

    for row in map:
        for tile in row:
            print(tile, end='')
        print()


map = (np.zeros((64, 64), dtype=int))
map = map.tolist()
convert_numbermap_to_map(map)
show_map(map)