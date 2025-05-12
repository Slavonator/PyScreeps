class Sector:

    def __init__(self, sector_map, x, y):
        self.sector_map = sector_map
        self.x, self.y = x, y
    
    def get_sector_map(self):
        return self.sector_map
    
    def get_position(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return(f'Sector({self.x}, {self.y})')
    
    def __str__(self):
        string_sector_map = ''
        for row in self.sector_map:
            for tile in row:
                string_sector_map += tile
            string_sector_map += '\n'
        return string_sector_map


class GameMap:

    def __init__(self):
        self.game_map = [[None]]
        self.x_indent, self.y_indent = 0, 0
        self.max_x, self.max_y, self.min_x, self.min_y = 0, 0, 0, 0
    
    def __str__(self):
        return str(self.game_map)
    
    def __iter__(self):
        return iter(self.game_map)
    
    def add_sector(self, sector: Sector):
        sector_x, sector_y = sector.get_position()
        if not (self.min_x <= sector_x <= self.max_x and self.min_y <= sector_y <= self.max_y):
            return
        # else:
        #     if self.min_x == sector_x
    
    def expand_map(self, direction):
        for symbol in direction:
            if symbol == 'n':
                self.game_map.insert(0, ['n'] * self.game_map_width)
                self.max_y += 1
            if symbol == 's':
                self.game_map.append(['s'] * self.game_map_width)
                self.min_y -= 1
            if symbol == 'e':
                for row in range(self.game_map_height):
                    self.game_map[row].append('e')
                self.max_x += 1
            if symbol == 'w':
                for row in range(self.game_map_height):
                    self.game_map[row].insert(0, 'w')
                self.min_x -= 1
    
    @property
    def game_map_width(self):
            return self.max_x - self.min_x + 1
    
    @property
    def game_map_height(self):
        return self.max_y - self.min_y + 1
    

if __name__ == '__main__':
    from map_generator import MapGenerator
    MAP_GENERATOR = MapGenerator()
    sector = Sector(MAP_GENERATOR.make_clear_map(), 0, 0)
    game_map = GameMap()
    for row in game_map:
        print(row)
