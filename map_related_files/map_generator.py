import numpy as np
if __package__:
    from .tiles import *
    from .game_map import *
else:
    from tiles import *
    from game_map import *

SIZE = 64  # Размер генерируемой карты
OBSTACLE_POINTS = 32  # Количество препятствий
OBSTACLE_SIZE = 4  # Размер препятствий
OBSTACLE_DENSITY = 0.7  # Вероятность появления препятствия в радиусе OBSTACLE_SIZE вокруг OBSTACLE_POINTS

OBSTACLE_PRESERVATION_THRESHOLD = 5  # Минимальное количество соседних препятствий,
# которое необходимо, чтобы препятствие не было сглажено
OBSTACLE_EXPANSION_THRESHOLD = 4 # Минимальное количество соседних препятствий,
# которое необходимо, чтобы пустая клетка стала препятствием в процессе сглаживания
SMOOTH_STEPS = 2  # Количество шагов сглаживания

RESOURCE_CHANCES = 0.05 # Вероятность появления ресурсов

# Значения по умолчанию:

# SIZE = 64
# OBSTACLE_POINTS = 32
# OBSTACLE_SIZE = 4
# OBSTACLE_DENSITY = 0.7
# OBSTACLE_PRESERVATION_THRESHOLD = 5
# OBSTACLE_EXPANSION_THRESHOLD = 4
# SMOOTH_STEPS = 2
# RESOURCE_CHANCES = 0.05


class MapGenerator:

    def __init__(
        self, 
        size=SIZE, 
        obstacle_points=OBSTACLE_POINTS, 
        obstacle_size=OBSTACLE_SIZE, 
        obstacle_density=OBSTACLE_DENSITY, 
        preservation_threshold=OBSTACLE_PRESERVATION_THRESHOLD,
        expansion_threshold=OBSTACLE_EXPANSION_THRESHOLD,
        smooth_steps=SMOOTH_STEPS,
        resource_chances=RESOURCE_CHANCES
    ):

        self.size = size
        self.obstacle_points = obstacle_points
        self.obstacle_size = obstacle_size
        self.obstacle_density = obstacle_density
        self.smooth_steps = smooth_steps
        self.preservation_threshold = preservation_threshold
        self.expansion_threshold = expansion_threshold
        self.resource_chances = resource_chances

    def generate_map(self):
        grid = self._generate_empty_grid()
        grid = self._generate_obstacles(grid)
        grid = self._place_resources(grid)
        return self._convert_array_to_game_map(grid)
    
    def make_clear_map(self):
        return self._convert_array_to_game_map(np.zeros((64, 64), dtype=np.int8))

    def _generate_empty_grid(self):

        grid = np.zeros((self.size, self.size), dtype=np.int8)

        return grid

    def _generate_obstacles(self, grid):

        centers = np.random.choice(self.size, (self.obstacle_points, 2))

        for y, x in centers:
            for dy in range(-self.obstacle_size, self.obstacle_size + 1):
                for dx in range(-self.obstacle_size, self.obstacle_size + 1):
                    if 0 <= y + dy < self.size and 0 <= x + dx < self.size:
                        if np.random.rand() < self.obstacle_density:
                            grid[y + dy, x + dx] = 1

        for _ in range(self.smooth_steps):

            neighbors = sum([
                np.roll(np.roll(grid, -1, 1), 1, 0),
                np.roll(np.roll(grid, 1, 1), -1, 0),
                np.roll(np.roll(grid, 1, 1), 1, 0),
                np.roll(np.roll(grid, -1, 1), -1, 0),
                np.roll(grid, 1, 1),
                np.roll(grid, -1, 1),
                np.roll(grid, 1, 0),
                np.roll(grid, -1, 0)
                ])

            grid = ((neighbors >= self.preservation_threshold) | (grid & neighbors >= self.expansion_threshold)).astype(np.int8)

        return grid

    def _place_resources(self, grid):
        contur = self._get_contur(grid)
        resources = ((contur == 1) & (np.random.rand(*grid.shape) < self.resource_chances))
        grid[resources] = 2
        return grid

    def _convert_array_to_game_map(self, array: np.ndarray):
        game_map = array.tolist()
        for x in range(self.size):
            for y in range(self.size):
                game_map[x][y] = convert_map_tile(game_map[x][y])
        return game_map

    @staticmethod
    def _get_contur(grid):

        neighbors = sum([
            np.roll(np.roll(grid, -1, 1), 1, 0),
            np.roll(np.roll(grid, 1, 1), -1, 0),
            np.roll(np.roll(grid, 1, 1), 1, 0),
            np.roll(np.roll(grid, -1, 1), -1, 0),
            np.roll(grid, 1, 1),
            np.roll(grid, -1, 1),
            np.roll(grid, 1, 0),
            np.roll(grid, -1, 0)
        ])

        return (grid & (0 < neighbors) & (neighbors < 8)).astype(np.int8)
    
