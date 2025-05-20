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
        move = self.can_move(direction)
        if move:
            self.x, self.y = move
            return True
        return False
    
    def can_move(self, direction: str) -> bool:

        new_x, new_y = self.x, self.y
        for symbol in direction:
            if symbol == 'n':
                new_y -= 1
            elif symbol == 's':
                new_y += 1
            elif symbol == 'e':
                new_x += 1
            elif symbol == 'w':
                new_x -= 1
            else:
                return False
            
            if not (0 <= new_x < 64 and 0 <= new_y < 64):
                # if not self._change_sectors((new_x, new_y)):
                    return False
            
            target_tile = self.sector.get_tile(new_x, new_y)

            if target_tile.get_walkspeed() == 0:
                return False
        
        return (new_x, new_y)
    
    # def _change_sectors(self, position: tuple):
    #     x, y = position
    #     sector_x, sector_y = self.sector.get_position()
    #     if x < 0:
    #         sector_x -= 1
    #         new_x = 63
    #     if x > 63:
    #         sector_x += 1
    #         new_x = 0
    #     if y < 0:
    #         sector_y -= 1
    #         new_y = 63
    #     if y > 63:
    #         sector_y += 1
    #         new_y = 0
    #     new_sector = GLOBAL_MAP.get_sector(sector_x, sector_y)
    #     if not new_sector:
    #         new_sector = Sector(
    #             GENERATOR.generate_map(),
    #             (sector_x, sector_y)
    #         )
    #         GLOBAL_MAP.add_sector(new_sector)
            

        
    def get_symbol(self):
        return self.symbol
    
    def get_position(self) -> tuple:
        return (self.x, self.y)

