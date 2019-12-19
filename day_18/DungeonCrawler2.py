import collections
import heapq
import numpy as np

class DungeonCrawler2:

    def __init__(self, raw_lines: [str]) -> None:
        self.dungeon = [s.rstrip() for s in raw_lines]
        single_line = ''.join(self.dungeon)

        w, h = len(self.dungeon[0]), len(self.dungeon)
        self.keys_to_find = set(c for c in single_line if c.islower())

        self.pos = list()
        bots = DungeonCrawler2.find_all_occurrences(single_line, '@')
        for bot in bots:
            self.pos.append((bot % w, bot // w))
        self.pos = tuple(self.pos)

    @staticmethod
    def find_all_occurrences(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def reachable_keys(self, x, y, keys):
        q = collections.deque([(x, y, 0)])
        seen = set()
        while q:
            cx, cy, distance = q.popleft()
            if self.dungeon[cy][cx].islower() and self.dungeon[cy][cx] not in keys:
                yield distance, cx, cy, self.dungeon[cy][cx]
                continue
            for d in range(1, 5):
                direction = DungeonCrawler2.direction(d)
                nx, ny = cx + direction[0], cy + direction[1]
                if (nx, ny) in seen:
                    continue
                seen.add((nx, ny))

                c = self.dungeon[ny][nx]
                if c != '#' and (not c.isupper() or c.lower() in keys):
                    q.append((nx, ny, distance + 1))

    def solve(self):
        q = [(0, self.pos, frozenset())]
        seen = [set(), set(), set(), set()]
        while q:
            d, current_pos, keys = heapq.heappop(q)
            if keys == self.keys_to_find:
                return d

            for i, (cx, cy) in enumerate(current_pos):
                if (cx, cy, keys) in seen[i]:
                    continue
                seen[i].add((cx, cy, keys))
                for l, nx, ny, key in self.reachable_keys(cx, cy, keys):
                    new_positions = current_pos[0:i] + ((nx, ny),) + current_pos[i + 1:]
                    heapq.heappush(q, (d + l, new_positions, keys | frozenset([key])))

    @staticmethod
    def direction(dir: int):
        if dir == 1:
            return np.array((0, -1))
        elif dir == 2:
            return np.array((0, 1))
        elif dir == 3:
            return np.array((-1, 0))
        elif dir == 4:
            return np.array((1, 0))