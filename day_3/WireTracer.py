from functools import reduce


class WireTracer:
    def __init__(self) -> None:
        self._wire_paths = list()

    def add_wire(self, wire_directions: [str]):
        wire_path = list()
        current_pos = (0, 0)

        for wire_direction in wire_directions:
            direction_string = wire_direction[:1]
            direction_vec = WireTracer.__vec_for_direction__(direction_string)
            length = int(wire_direction[1:])

            for i in range(length):
                current_pos = (current_pos[0] + direction_vec[0], current_pos[1] + direction_vec[1])
                wire_path.append(current_pos)

        self._wire_paths.append(wire_path)

    def get_closest_intersection(self) -> [tuple]:
        intersections = self.__get_intersections__()
        intersections.sort(key=lambda tup: abs(tup[0]) + abs(tup[1]))
        return intersections[0]

    def __get_intersections__(self):
        wire_path_sets = list()
        for path in self._wire_paths:
            wire_path_sets.append(set(path))

        return list(set.intersection(*wire_path_sets))

    def get_closest_intersection_distance(self):
        intersection = self.get_closest_intersection()
        return abs(intersection[0]) + abs(intersection[1])

    def get_shortest_path_to_intersection(self) -> int:
        intersections = self.__get_intersections__()
        intersections_with_path_lengths = list()

        for intersection in intersections:
            path_lengths = list()

            for path in self._wire_paths:
                length = WireTracer.__get_path_length_to_intersection__(path, intersection)
                path_lengths.append(length)

            intersections_with_path_lengths.append({
                'intersection': intersection,
                'path_lengths': path_lengths,
                'combined_length': WireTracer.__calculate_combined_path_length__(path_lengths)
            })

        intersections_with_path_lengths.sort(
            key=lambda intersection_with_lengths: intersection_with_lengths['combined_length']
        )

        return intersections_with_path_lengths[0]['combined_length']

    @staticmethod
    def __calculate_combined_path_length__(lenghts: [int]) -> int:
        return reduce(lambda l, r: l + r, lenghts)

    @staticmethod
    def __get_path_length_to_intersection__(wire_path: [tuple], intersection: tuple):
        assert intersection in wire_path

        return 1 + wire_path.index(intersection)

    @staticmethod
    def __vec_for_direction__(direction_str: str) -> tuple:
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

