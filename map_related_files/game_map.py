if __package__:
    from .tiles import *
else:
    from tiles import *

class Sector:

    def __init__(self, sector_map: list[list[Tile]], x_y_position: tuple[int, int]) -> None:
        self.sector_map = sector_map
        self.x, self.y = x_y_position

    def __iter__(self):
        return iter(self.sector_map)
    
    def get_sector_map(self) -> list:
        return self.sector_map
    
    def get_position(self) -> tuple:
        return (self.x, self.y)
    
    def __repr__(self) -> str:
        return(f'Sector({self.x}, {self.y})')
    
    def __str__(self) -> str:
        string_sector_map = ''
        for row in self.sector_map:
            for tile in row:
                string_sector_map += str(tile)
            string_sector_map += '\n'
        return string_sector_map


class GameMap:

    def __init__(self) -> None:
        self.game_map = [[None]]
        self.x_indent, self.y_indent = 0, 0
        self.max_x, self.max_y, self.min_x, self.min_y = 0, 0, 0, 0
    
    def __str__(self) -> str:
        return str(self.game_map)
    
    def __iter__(self):
        return iter(self.game_map)

    def add_sector(self, sector: Sector) -> None:
        sector_x, sector_y = sector.get_position()
        while self.min_x > sector_x:
            self.expand_map('w')
        while self.max_x < sector_x:
            self.expand_map('e')
        while self.min_y > sector_y:
            self.expand_map('s')
        while self.max_y < sector_y:
            self.expand_map('n')
        self.game_map[self.max_y - sector_y][sector_x - self.min_x] = sector
    
    def expand_map(self, direction):
        for symbol in direction:
            if symbol == 'n':
                self.game_map.insert(0, [None] * self.game_map_width)
                self.max_y += 1
            if symbol == 's':
                self.game_map.append([None] * self.game_map_width)
                self.min_y -= 1
            if symbol == 'e':
                for row in range(self.game_map_height):
                    self.game_map[row].append(None)
                self.max_x += 1
            if symbol == 'w':
                for row in range(self.game_map_height):
                    self.game_map[row].insert(0, None)
                self.min_x -= 1

    def get_sector(self, x, y):
        if self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y:
            return self.game_map[self.max_y - y][x - self.min_x]
    
    @property
    def game_map_width(self):
            return self.max_x - self.min_x + 1
    
    @property
    def game_map_height(self):
        return self.max_y - self.min_y + 1
    
