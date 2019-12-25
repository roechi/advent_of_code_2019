import numpy as np

class BugPopulation:
    def __init__(self, raw_grid: [str]) -> None:
        raw_grid = list(map(lambda s: s.rstrip(), raw_grid))
        width = len(raw_grid[0])
        height = len(raw_grid)

        grid = [[None for x in range(width)] for y in range(height)]

        for y in range(height):
            for x in range(width):
                grid[y][x] = 1 if raw_grid[y][x] == '#' else 0

        self.grid = grid
        self.states = list()
        self.states.append(grid)
        self.directions = [(0, 1), (1, 0), (0, - 1), (-1, 0)]
        self.width = width
        self.height = height
        self.layers = dict()
        self.layers[0] = grid
        self.cycles = 0
        self.min_layer = 0
        self.max_layer = 0

    @staticmethod
    def get_edge_tiles(dir: tuple):
        edge_tiles = list()
        if dir == (0, 1):
            for i in range(5):
                edge_tiles.append(tuple(np.array((0, 0)) + (i * np.array((1, 0)))))
        elif dir == (0, -1):
            for i in range(5):
                edge_tiles.append(tuple(np.array((0, 4)) + (i * np.array((1, 0)))))
        elif dir == (1, 0):
            for i in range(5):
                edge_tiles.append(tuple(np.array((0, 0)) + (i * np.array((0, 1)))))
        elif dir == (-1, 0):
            for i in range(5):
                edge_tiles.append(tuple(np.array((4, 0)) + (i * np.array((0, 1)))))
        return edge_tiles

    def cycle(self):
        if self.cycles % 2 == 0:
            self.layers[self.min_layer - 1] = [[0 for x in range(self.width)] for y in range(self.height)]
            self.layers[self.max_layer + 1] = [[0 for x in range(self.width)] for y in range(self.height)]
            self.min_layer -= 1
            self.max_layer += 1

        new_layers = self.layers.copy()

        levels_to_cycle = list(new_layers.keys())
        for l in levels_to_cycle:
            new_grid = [[0 for x in range(self.width)] for y in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
                    if (y, x) != (2, 2):
                        adjacent_pop = 0
                        for d in self.directions:
                            pos = tuple(np.array((y, x)) + np.array(d))
                            if 0 <= pos[0] < self.height and 0 <= pos[1] < self.width:
                                if pos == (2, 2) and l > self.min_layer:
                                    inner_grid = self.layers[l - 1]
                                    edge_tiles = BugPopulation.get_edge_tiles(d)
                                    for t in edge_tiles:
                                        if inner_grid[t[0]][t[1]] == 1:
                                            adjacent_pop += 1

                                elif self.layers[l][pos[0]][pos[1]] == 1:
                                    adjacent_pop += 1
                            if (0 > pos[0] or 0 > pos[1] or self.width == pos[1] or self.height == pos[0]) and l < self.max_layer:
                                outer_grid = self.layers[l + 1]
                                pos = tuple(np.array((2, 2)) + np.array(d))
                                if outer_grid[pos[0]][pos[1]] == 1:
                                    adjacent_pop += 1

                        if self.layers[l][y][x] == 1 and adjacent_pop == 1:
                            new_grid[y][x] = 1
                        elif self.layers[l][y][x] == 0 and adjacent_pop in [1, 2]:
                            new_grid[y][x] = 1
                        else:
                            new_grid[y][x] = 0

            new_layers[l] = new_grid

        self.layers = new_layers
        self.cycles += 1


    def get_total_bug_count(self):
        bug_count = 0
        for k in self.layers.keys():
            grid = self.layers[k]
            for l in grid:
                bug_count += sum(l)

        return bug_count

    def check_duplicates(self):
        dupes = [x for n, x in enumerate(self.states) if x in self.states[:n]]
        if dupes:
            return dupes
        else:
            return None

    def cycle_until_duplicate(self):

        while True:
            self.cycle()
            dupes = self.check_duplicates()
            if dupes:
                break

        dupe = dupes[0]

        linear = []
        for l in dupe:
            linear.extend(l)

        rating = 0
        for i in range(len(linear)):
            if linear[i] == 1:
                rating += pow(2, i)

        return rating