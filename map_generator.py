import numpy as np


def generate_map_sector():
    
    grid = np.zeros((SIZE, SIZE), dtype=int)

    centers = np.random.choice(SIZE, (OBSTACLE_POINTS, 2))

    for y, x in centers:
        for dy in range(-OBSTACLE_SIZE, OBSTACLE_SIZE + 1):
            for dx in range(-OBSTACLE_SIZE, OBSTACLE_SIZE + 1):
                if 0 <= y + dy < SIZE and 0 <= x + dx < SIZE:
                    if np.random.rand() < OBSTACLE_DENSITY:
                        grid[y + dy, x + dx] = 1

    for _ in range(SMOOTH_STEPS):

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

        grid = ((neighbors >= 5) | (grid & neighbors >= 4)).astype(int)

    return grid


SIZE = 64
OBSTACLE_POINTS = 6
OBSTACLE_SIZE = 8
OBSTACLE_DENSITY = 0.5
SMOOTH_STEPS = 2


if __name__ == "__main__":
    with np.printoptions(threshold=np.inf, linewidth=199):
        print(generate_map_sector())

