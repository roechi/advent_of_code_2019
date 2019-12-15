from day_13.IntcodeComputer import IntcodeComputer
import numpy as np

from day_6.MapNavigator import Node


class RepairDroid:
    def __init__(self, program: [int]) -> None:
        self.computer = IntcodeComputer(program)
        self.map = dict()

    def find(self):
        seen = dict()
        pos = np.array((0, 0))
        all_seen = False
        while not all_seen:
            has_to_backtrack = True
            for i in [1, 4, 2, 3]:
                if tuple(pos + RepairDroid.direction(i)) not in seen:
                    has_to_backtrack = False
                    mem, out, exit_code = self.computer.run_program(input=[i], reset_relative_pointer=False,
                                                                    reset_pointer=False, reset_memory=False)
                    assert len(out) == 1
                    out_code = out[0]
                    if out_code == 0:
                        seen[tuple(pos + RepairDroid.direction(i))] = '#'
                    elif out_code == 1:
                        pos += RepairDroid.direction(i)
                        seen[tuple(pos)] = '.'
                    elif out_code == 2:
                        pos += RepairDroid.direction(i)
                        seen[tuple(pos)] = '+'
                    break

            if has_to_backtrack:
                path = list()
                path.append(tuple(pos))
                commands = RepairDroid.backtrack(seen, path, list())
                for i in commands[0]:
                    mem, out, exit_code = self.computer.run_program(input=[i], reset_relative_pointer=False,
                                                                    reset_pointer=False, reset_memory=False)
                    if out[0] != 0:
                        pos += RepairDroid.direction(i)

                    else:
                        print('Backtracking failed!')
                all_seen = has_to_backtrack and not commands[0]

        RepairDroid.print_screen(seen, tuple(pos))

        self.map = seen

        tree = RepairDroid.BFS(seen)

        path_to_oxygen = list()

        while tree.parent:
            path_to_oxygen.append(tree.data[0])
            tree = tree.parent

        target_pos = None
        shortest_path_map = seen.copy()
        for pos in path_to_oxygen:
            if pos != (0, 0) and shortest_path_map[pos] != '+':
                shortest_path_map[pos] = 'X'
            elif shortest_path_map[pos] == '+':
                target_pos = pos
        RepairDroid.print_screen(shortest_path_map, tuple(pos))
        print('Target: {}'.format(target_pos))

        return path_to_oxygen, target_pos

    @staticmethod
    def BFS(map: dict):
        tree = Node(((0,0), 'O'))
        discovered = list()
        q = list()
        discovered.append(tree.data[0])
        q.append(tree)
        while q:
            v = q.pop()
            if v.data[1] == '+':
                return v
            children = list()
            for i in range(1, 5):
                pos_to_check = tuple(np.array(v.data[0]) + RepairDroid.direction(i))
                if pos_to_check in map and pos_to_check not in discovered:
                    if map[pos_to_check] != '#':
                        children.append(pos_to_check)
            for c in children:
                if c not in discovered:
                    discovered.append(c)
                    node = Node((c, map[c]))
                    v.add_node(v, node)
                    q.append(node)

    def oxygenate(self, oxygen_pos: tuple):
        pos_map = self.map.copy()
        pos_map[oxygen_pos] = 'O'
        minutes = 0
        #self.print_screen(pos_map, (0, 0))
        while '.' in pos_map.values():
            #self.print_screen(pos_map, (0, 0))
            minutes += 1

            pos_to_oxygenate = list()
            for pos in pos_map.keys():
                if pos_map[pos] == 'O':
                    pos_to_oxygenate.append(pos)

            for pos in pos_to_oxygenate:
                if pos_map[pos] == 'O':
                    for i in range(1, 5):
                        pos_to_check = tuple(np.array(pos) + RepairDroid.direction(i))
                        if pos_to_check in pos_map and pos_map[pos_to_check] == '.':
                            pos_map[pos_to_check] = 'O'
        return minutes



    @staticmethod
    def backtrack(seen: dict, path: list, path_commands: list):
        found = False
        for i in [1, 4, 2, 3]:
            if not found:
                field = np.array(path[-1:][0]) + RepairDroid.direction(i)
                if tuple(field) in seen:
                    if seen[tuple(field)] != '#' and tuple(field) not in path:
                        path.append(tuple(field))
                        path_commands.append(i)
                        path_commands, found = RepairDroid.backtrack(seen, path, path_commands)
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
    def print_screen(seen: dict, pos: tuple):
        if seen and pos:
            x_max = max(map(lambda t: t[0], seen.keys()))
            x_min = min(map(lambda t: t[0], seen.keys()))
            y_max = max(map(lambda t: t[1], seen.keys()))
            y_min = min(map(lambda t: t[1], seen.keys()))

            for y in range(y_min, y_max + 1):
                line = ''
                for x in range(x_min, x_max + 1):
                    if (x, y) == (0, 0):
                        line += 'O'
                    else:
                        if (x, y) != pos:
                            if (x, y) in seen:
                                line += seen[(x, y)]
                            else:
                                line += ' '
                        else:
                            line += 'x'
                print(line)
            print('----------------------------------')

