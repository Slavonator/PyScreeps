from resources import Iron

class Tile:

    def __init__(
            self, 
            symbol: str,
            walkspeed: int,
            contains: list | None=None,
            minable: bool=False
            ):
        
        self.symbol = symbol
        self.walkspeed = walkspeed
        self.contains = contains if contains is not None else []
        self.mineable = minable

    def __repr__(self):
        return self.symbol
    
    def get_minable(self):
        return self.mineable
    
    def get_walkspeed(self):
        return self.walkspeed
    
    def get_contains(self):
        return self.contains


class EmptyTile(Tile):

    def __init__(self):
        super().__init__(" ", 5)


class ObstacleTile(Tile):

    def __init__(self):
        super().__init__("w", 0)


class RoadTile(Tile):

    def __init__(self):
        super().__init__("#", 10)


class BasicOre(ObstacleTile):

    def __init__(self):
        super().__init__()
        self.symbol = 'o'
        self.contains = [Iron]
        self.mineable = True


MAP_TILES_DICT = {
    0: EmptyTile,
    1: ObstacleTile,
    2: BasicOre,
    3: RoadTile
}