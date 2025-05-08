from map_related_files import *
import numpy as np

GENERATOR = map_generator.MapGenerator()

def show_map(map):

    for row in map:
        for tile in row:
            print(tile, end='')
        print()
