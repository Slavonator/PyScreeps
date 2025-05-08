from .resources import *
from datetime import timedelta, datetime

# Классы

class Tile:

    __slots__ = (
        "symbol",
        "walkspeed",
        "contains",
        "mineable",
        "destructable"
    )

    def __init__(
            self, 
            symbol: str="?",
            walkspeed: int=1,
            contains: list | None=None,
            mineable: bool=False,
            destructable: bool=False
        ):
        
        self.symbol = symbol
        self.walkspeed = walkspeed
        self.contains = contains if contains is not None else []
        self.mineable = mineable
        self.destructable = destructable

    def __str__(self):
        return self.symbol
    
    def __repr__(self):
        return f'{self.__class__.__name__}(symbol={self.symbol})'
    
    def get_mineable(self):
        return self.mineable
    
    def get_walkspeed(self):
        return self.walkspeed
    
    def get_contains(self):
        return self.contains
    
    def get_destructable(self):
        return self.destructable
    
    def mine(self):
        if self.get_mineable():
            if self.get_timeout_state():
                return 'Уже добыто'
            else:
                self.timed_out = datetime.now()
        else:
            return 'Нечего добывать'


class EmptyTile(Tile):

    def __init__(self):
        super().__init__(
            symbol=".",
            walkspeed=5
        )


class ObstacleTile(Tile):

    def __init__(self):
        super().__init__(
            symbol='O',
            walkspeed=0
        )


class Deposit(Tile):

    __slots__ = (
        "resource"
        "timed_out"
    )

    def __init__(self,
        symbol: str='D',
        resource: Resource=Resource):
        super().__init__(
            symbol=symbol,
            walkspeed=0,
            mineable=True
        )
        self.resource = resource
        self.timed_out = False

    def get_timeout_state(self):
        if self.timed_out:
            if datetime.now() - self.timed_out > self.resource.get_timeout():
                self.timed_out = False
        return self.timed_out


class IronDeposit(Deposit):

    def __init__(self):
        super().__init__(
            symbol='I',
            resource=Iron()
        )

# Функции

def convert_map_tile(tile_index: int):
    if tile_index == 0:
        return EmptyTile()
    if tile_index == 1:
        return OBSTACLE
    if tile_index == 2:
        return IronDeposit()
    return Tile()

# Константы

OBSTACLE = ObstacleTile()
