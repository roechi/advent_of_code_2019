import sys

import numpy as np

class DungeonCrawler3:
    def __init__(self, raw_lines: [str], folded: bool = False) -> None:
        d = raw_lines
        width, height = len(d[0]), len(d)

        self.dungeon = dict()

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        single_line = ''.join(self.dungeon)

        portals = dict()

        for y in range(height):
            for x in range(width):
                if d[y][x].isupper():
                    first = d[y][x]
                    for dir in self.directions:

                        if 0 <= y + dir[0] < height and 0 <= x + dir[1] < width:
                            if d[y + dir[0]][x + dir[1]].isupper():
                                second = d[y + dir[0]][x + dir[1]]
                                if 0 <= y + 2 * dir[0] < height and 0 <= x + 2 * dir[1] < width and d[y + 2 * dir[0]][x + 2 * dir[1]] == '.':
                                    portal_coord = (y + 2 * dir[0], x + 2 * dir[1])
                                    if dir[0] + dir[1] > 0:
                                        portal_id = first + second
                                    else:
                                        portal_id = second + first

                                    if portal_coord not in portals:
                                        portals[portal_coord] = portal_id

                elif d[y][x] != ' ' and d[y][x] != '_':
                    self.dungeon[(y, x)] = d[y][x]

        self.portals = portals
        self.width = width
        self.height = height
        self.folded = folded

    def dijkstra(self, start: tuple, target: tuple):
        if not self.folded:
            return self.__dijkstra__(start, target)
        else:
            depth = 0
            while True:
                dist = self.__dijkstra_folded__(start, target, max_depth=depth)
                if dist[0] < sys.maxsize:
                    return dist[0]
                else:
                    depth += 1

    def __dijkstra__(self, start: tuple, target: tuple):
        distances = dict()
        distances[start] = 0
        q = list()
        q.append(start)
        for v in self.dungeon.keys():
            c = self.dungeon[v]
            if c != '#' and v != start:
                distances[v] = sys.maxsize
                q.append(v)

        while q:
            q.sort(key=lambda t: distances[t])
            u = q.pop()
            for d in self.directions:
                v = tuple(np.array(u) + np.array(d))
                if v in self.dungeon and self.dungeon[v] not in ['#', '\n']:
                    alt = distances[u] + 1
                    if alt < distances[v] or distances[v] == sys.maxsize:
                        distances[v] = alt
                        if v in q:
                            q.remove(v)
                        q.append(v)
            if u in self.portals.keys():
                portal_id = self.portals[u]
                for p in self.portals.keys():
                    if p != u and self.portals[p] == portal_id:
                        v = p
                        break
                if v in self.dungeon and self.dungeon[v] == '.':
                    alt = distances[u] + 1
                    if alt < distances[v] or distances[v] == sys.maxsize:
                        distances[v] = alt
                        if v in q:
                            q.remove(v)
                        q.append(v)


        return distances[target]

    def __dijkstra_folded__(self, start: tuple, target: tuple, max_depth: int = 0):
        distances = dict()
        distances[(start, 0)] = (0, 0)
        q = list()
        q.append((start, 0))
        for v in self.dungeon.keys():
            c = self.dungeon[v]
            if c != '#' and v != start:
                distances[(v, 0)] = (sys.maxsize, 0)
                q.append((v, 0))

        while q:
            q.sort(key=lambda t: distances[t][0])
            q.sort(key=lambda t: distances[t][1])

            u = q.pop()
            for d in self.directions:
                v = (tuple(np.array(u[0]) + np.array(d)), u[1])
                if v[0] in self.dungeon and self.dungeon[v[0]] not in ['#', '\n'] and \
                        ((u[1] == 0 or not self.is_outer_portal(v[0])) or (u[1] != 0) and not self.is_entrance_or_exit(v[0])):
                    alt = distances[u][0] + 1
                    if v not in distances:
                        distances[v] = (sys.maxsize, v[1])
                    if alt < distances[v][0] or distances[v][0] == sys.maxsize:
                        distances[v] = (alt, v[1])
                        if v in q:
                            q.remove(v)
                        q.append(v)
            if u[0] in self.portals.keys():
                if u[1] == 0:
                    if not self.is_outer_portal(u[0]):
                        portal_id = self.portals[u[0]]
                        for p in self.portals.keys():
                            if p != u[0] and self.portals[p] == portal_id:
                                v = (p, u[1] + 1)
                                break
                        if v[0] in self.dungeon and self.dungeon[v[0]] == '.':
                            alt = distances[u][0] + 1
                            if v not in distances:
                                distances[v] = (sys.maxsize, v[1])
                            if alt < distances[v][0] or distances[v][0] == sys.maxsize:
                                distances[v] = (alt, v[1])
                                if v in q:
                                    q.remove(v)
                                q.append(v)
                else:
                    if not self.is_outer_portal(u[0]) and u[1] < max_depth:
                        portal_id = self.portals[u[0]]
                        for p in self.portals.keys():
                            if p != u[0] and self.portals[p] == portal_id:
                                v = (p, u[1] + 1)
                                break
                        if v[0] in self.dungeon and self.dungeon[v[0]] == '.':
                            alt = distances[u][0] + 1
                            if v not in distances:
                                distances[v] = (sys.maxsize, v[1])
                            if alt < distances[v][0] or distances[v][0] == sys.maxsize:
                                distances[v] = (alt, v[1])
                                if v in q:
                                    q.remove(v)
                                q.append(v)
                    elif self.is_outer_portal(u[0]) and not self.is_entrance_or_exit(u[0]):
                        portal_id = self.portals[u[0]]
                        for p in self.portals.keys():
                            if p != u[0] and self.portals[p] == portal_id:
                                v = (p, u[1] - 1)
                                break
                        if v[0] in self.dungeon and self.dungeon[v[0]] == '.':
                            alt = distances[u][0] + 1
                            if v not in distances:
                                distances[v] = (sys.maxsize, v[1])
                            if alt < distances[v][0] or distances[v][0] == sys.maxsize:
                                distances[v] = (alt, v[1])
                                if v in q:
                                    q.remove(v)
                                q.append(v)

        return distances[(target, 0)]


    def is_outer_portal(self, pos: tuple):
        if pos[0] == 2 or pos[0] == self.height - 3 or pos[1] == 2 or pos[1] == self.width - 3:
            return True
        else:
            return False

    def is_entrance_or_exit(self, pos: tuple):
        if self.portals[pos] in ['AA', 'ZZ']:
            return True
        else:
            return False