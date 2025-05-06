from .tiles import *

class GameMap:

    def __init__(self, grid):
        self.grid = grid

    def place_tile(self, x, y, tile: Tile):
        self.grid[x, y] = MAP_TILES.index(tile)

