from day_6.MapNavigator import Node
import numpy as np
import sys

class DungeonCrawler:
    def __init__(self, map_str: [str]) -> None:
        self.map, self.keys, self.doors, self.droid_pos = DungeonCrawler.parse_map_str(map_str)
        DungeonCrawler.print_screen(self.map, self.droid_pos)

    def solve(self):
        all_remaining_targets = dict()
        all_remaining_targets.update(self.keys)
        all_remaining_targets.update(self.doors)
        all_paths = []
        pos = self.droid_pos

        DungeonCrawler.find_next(self.map.copy(), pos, all_remaining_targets, list(), list(), all_paths, len(self.keys))

        all_paths.sort(key=lambda p: len(p))
        return len(all_paths[0])


    @staticmethod
    def find_next(dungeon: dict, pos: tuple, remaining_targets: dict, collected_keys: [str], current_path: [tuple], total_paths: [[tuple]], num_of_keys_to_find: int):
        if not remaining_targets or all(['A' <= target <= 'B' for target in remaining_targets]):
            if num_of_keys_to_find == len(collected_keys):
                total_paths.append(current_path)
        else:
            paths = dict()
            for target in remaining_targets:
                if not 'A' <= target <= 'Z' or target.lower() in collected_keys:
                    path_tree = DungeonCrawler.dijkstra(dungeon, pos, remaining_targets[target], collected_keys)[1]
                    if path_tree:
                        resolved_path = list()
                        while path_tree.parent is not None:
                            resolved_path.append(path_tree.data)
                            path_tree = path_tree.parent
                        resolved_path.reverse()

                        blocked = False
                        path = list()
                        while resolved_path and not blocked:
                            current_pos = resolved_path.pop()
                            if 65 <= ord(dungeon[current_pos]) <= 90 and dungeon[current_pos] != target:
                                blocked = True
                            else:
                                path.append(current_pos)

                        if not blocked:
                            paths[target] = path

            for path_key in paths.keys():
                if not 65 <= ord(path_key) <= 90 or path_key.lower() in collected_keys:
                    dun = dungeon.copy()
                    coll = collected_keys.copy()
                    p = current_path.copy()
                    rem = remaining_targets.copy()
                    next_pos = remaining_targets[path_key]
                    if 97 <= ord(path_key) <= 122:
                        coll.append(path_key)
                    dun[rem[path_key]] = '.'
                    rem.pop(path_key)
                    p.extend(paths[path_key])
                    DungeonCrawler.find_next(dun, next_pos, rem, coll, p, total_paths, num_of_keys_to_find)

    @staticmethod
    def parse_map_str(map_str: [str]):
        parsed_map = dict()
        key_positions = dict()
        door_positions = dict()
        droid_position = (0, 0)


        for y in range(len(map_str)):
            for x in range(len(map_str[y])):
                parsed_map[(x, y)] = map_str[y][x]
                if parsed_map[(x, y)] == '\n':
                    parsed_map[(x, y)] = ' '
                elif 97 <= ord(parsed_map[(x, y)]) <= 122:
                    key_positions[parsed_map[(x, y)]] = (x, y)
                elif 65 <= ord(parsed_map[(x, y)]) <= 90:
                    door_positions[parsed_map[(x, y)]] = (x, y)
                elif parsed_map[(x, y)] == '@':
                    droid_position = (x, y)
                    parsed_map[(x, y)] = '.'

        return parsed_map, key_positions, door_positions, droid_position

    @staticmethod
    def BFS(map: dict, start: tuple, target: tuple):
        tree = Node(start)
        discovered = list()
        q = list()
        discovered.append(tree.data)
        q.append(tree)
        while q:
            v = q.pop()
            if v.data == target:
                return v
            children = list()
            for i in range(1, 5):
                pos_to_check = tuple(np.array(v.data) + DungeonCrawler.direction(i))
                if pos_to_check in map and map[pos_to_check] != '#' and (map[pos_to_check] < 'A' or map[pos_to_check] > 'Z') and pos_to_check not in discovered:
                    children.append(pos_to_check)
            for c in children:
                if c not in discovered:
                    discovered.append(c)
                    node = Node(c)
                    v.add_node(v, node)
                    q.append(node)

    @staticmethod
    def dijkstra(dungeon: dict, start: tuple, target: tuple, keys: list):
        distances = dict()
        distances[start] = 0
        tree = Node(start)
        target_leaf = None
        q = list()
        q.append(start)
        for v in dungeon.keys():
            c = dungeon[v]
            if c != '#' and v != start:
                distances[v] = sys.maxsize
                q.append(v)

        while q:
            q.sort(key=lambda t: distances[t])
            u = q.pop()
            for i in range(1, 5):
                v = tuple(np.array(u) + DungeonCrawler.direction(i))
                if v in dungeon and dungeon[v] not in ['#', '\n']:
                    if not ('A' <= dungeon[v] <= 'Z') or dungeon[v].lower() in keys:
                        alt = distances[u] + 1
                        if alt < distances[v] or distances[v] == sys.maxsize:
                            distances[v] = alt
                            v_node = tree.add(u, v)
                            if v == target:
                                target_leaf = v_node
                            if v in q:
                                q.remove(v)
                            q.append(v)


        return distances[target], target_leaf


    @staticmethod
    def backtrack(seen: dict, path: list, path_commands: list):
        found = False
        for i in [1, 4, 2, 3]:
            if not found:
                field = np.array(path[-1:][0]) + DungeonCrawler.direction(i)
                if tuple(field) in seen:
                    if seen[tuple(field)] != '#' and tuple(field) not in path:
                        path.append(tuple(field))
                        path_commands.append(i)
                        path_commands, found = DungeonCrawler.backtrack(seen, path, path_commands)
                else:
                    return path_commands, True
        if not found and path_commands:
            path_commands.pop()
            path.pop()
        return path_commands, found


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

    @staticmethod
    def get_reverse_direction(dir: int):
        if dir == 1:
            return 2
        elif dir == 2:
            return 1
        elif dir == 3:
            return 4
        elif dir == 4:
            return 3

    @staticmethod
    def print_screen(dungeon_map: dict, pos: tuple):
        if dungeon_map and pos:
            x_max = max(map(lambda t: t[0], dungeon_map.keys()))
            x_min = min(map(lambda t: t[0], dungeon_map.keys()))
            y_max = max(map(lambda t: t[1], dungeon_map.keys()))
            y_min = min(map(lambda t: t[1], dungeon_map.keys()))

            for y in range(y_min, y_max + 1):
                line = ''
                for x in range(x_min, x_max + 1):
                        if (x, y) != pos:
                            if (x, y) in dungeon_map:
                                line += dungeon_map[(x, y)]
                            else:
                                line += ' '
                        else:
                            line += '@'
                print(line)
            print('----------------------------------')