class WireTracer:
    def __init__(self) -> None:
        self.wire_paths = list()

    def add_wire(self, wire_directions: [str]):
        wire_path = list()
        current_pos = (0, 0)

        for wire_direction in wire_directions:
            direction_string = wire_direction[:1]
            direction_vec = WireTracer.vec_for_direction(direction_string)
            length = int(wire_direction[1:])

            for i in range(length):
                current_pos = (current_pos[0] + direction_vec[0], current_pos[1] + direction_vec[1])
                wire_path.append(current_pos)

        self.wire_paths.append(wire_path)

    def get_closest_intersection(self):
        wire_path_sets = list()
        for path in self.wire_paths:
            wire_path_sets.append(set(path))

        intersections = list(set.intersection(*wire_path_sets))
        intersections.sort(key=lambda tup: abs(tup[0]) + abs(tup[1]))
        return intersections[0]

    def get_closest_intersection_distance(self):
        intersection = self.get_closest_intersection()
        return abs(intersection[0]) + abs(intersection[1])

    @staticmethod
    def vec_for_direction(direction_str: str) -> tuple:
        if direction_str == 'U':
            return 0, 1
        elif direction_str == 'R':
            return 1, 0
        elif direction_str == 'D':
            return 0, -1
        elif direction_str == 'L':
            return -1, 0
        else:
            raise Exception('Received illegal direction string: ' + str(direction_str))

