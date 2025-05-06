from .resources import *

# Динамические клетки:

class Tile:

    __slots__ = ("symbol", "walkspeed", "contains", "resource", "destructable")

    def __init__(
            self, 
            symbol: str="?",
            walkspeed: int=1,
            contains: list | None=None,
            resource: None | Resource=None,
            destructable: bool=False
        ):
        
        self.symbol = symbol
        self.walkspeed = walkspeed
        self.contains = contains if contains is not None else []
        self.resource = resource
        self.destructable = destructable

    def __str__(self):
        return self.symbol
    
    def get_resource(self):
        return self.resource
    
    def get_walkspeed(self):
        return self.walkspeed
    
    def get_contains(self):
        return self.contains
    
    def get_destructable(self):
        return self.destructable
    
    def mine(self):
        if self.get_resource():
            ...
        else:
            return 'Нечего добывать'



class EmptyTile(Tile):

    def __init__(self):
        super().__init__(".", 5)



class Deposit(Tile):

    def __init__(self,
        symbol: str='D',
        resource: Resource=Resource):
        super().__init__(
            symbol=symbol,
            walkspeed=0,
            resource=resource
        )


class IronDeposit(Deposit):

    def __init__(self):
        super().__init__('I', Iron)

# Статические клетки

class ObstacleTile(Tile):

    __slots__ = ()

    def __init__(self):
        super().__init__(
            symbol='O',
            walkspeed=0,
            resource=False,
            destructable=False
        )

# Константы

OBSTACLE = ObstacleTile()

MAP_TILES = (
        EmptyTile(),
        OBSTACLE,
        Deposit(),
        )

