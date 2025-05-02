import numpy as np

SIZE = 64
OBSTACLE_POINTS = 32
OBSTACLE_SIZE = 4
OBSTACLE_DENSITY = 0.7
OBSTACLE_PRESERVATION_THRESHOLD = 5
OBSTACLE_EXPANSION_THRESHOLD = 4
SMOOTH_STEPS = 2

# Значения по умлочанию:
# SIZE = 64
# OBSTACLE_POINTS = 32
# OBSTACLE_SIZE = 4
# OBSTACLE_DENSITY = 0.7
# OBSTACLE_PRESERVATION_THRESHOLD = 5
# OBSTACLE_EXPANSION_THRESHOLD = 4
# SMOOTH_STEPS = 2


class MapGenerator:

    def __init__(
        self, 
        size=SIZE, 
        obstacle_points=OBSTACLE_POINTS, 
        obstacle_size=OBSTACLE_SIZE, 
        obstacle_density=OBSTACLE_DENSITY, 
        preservation_threshold=OBSTACLE_PRESERVATION_THRESHOLD,
        expansion_threshold=OBSTACLE_EXPANSION_THRESHOLD,
        smooth_steps=SMOOTH_STEPS
    ):

        self.size = size
        self.obstacle_points = obstacle_points
        self.obstacle_size = obstacle_size
        self.obstacle_density = obstacle_density
        self.smooth_steps = smooth_steps
        self.preservation_threshold = preservation_threshold
        self.expansion_threshold = expansion_threshold

    def __call__(self):
        return self._generate_map()

    def _generate_map(self):

        grid = np.zeros((self.size, self.size), dtype=int)

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

            grid = ((neighbors >= self.preservation_threshold) | (grid & neighbors >= self.expansion_threshold)).astype(int)

        return grid


if __name__ == "__main__":
    with np.printoptions(threshold=np.inf, linewidth=200):
        import os
        os.system("clear")
        f = open("output.txt", "w+")
        mg = MapGenerator()
        f.write(str(mg()))
