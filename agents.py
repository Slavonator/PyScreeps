from map_related_files.game_map import Sector

class Agent:
    
    def __init__(self, sector: Sector, position: tuple, symbol: str='A'):
        self.sector = sector
        x, y = position
        self.x = x
        self.y = y
        self.symbol = symbol
        self.inventory = []

    def move(self, direction: str) -> bool:
        new_x, new_y = self.x, self.y
        
        if direction == 'n':
            new_y -= 1
        elif direction == 's':
            new_y += 1
        elif direction == 'e':
            new_x += 1
        elif direction == 'w':
            new_x -= 1
        else:
            return False

        if not (0 <= new_x < 64 and 0 <= new_y < 64):
            return False
        
        target_tile = self.sector.get_tile(new_x, new_y)

        if target_tile.get_walkspeed() == 0:
            return False
        
        self.x, self.y = new_x, new_y
        return True
    
    def get_symbol(self):
        return self.symbol
    
    def get_position(self) -> tuple:
        return (self.x, self.y)