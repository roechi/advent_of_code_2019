import numpy as np
from numpy.linalg import norm
from numpy import dot
import sys


class AsteroidScanner:
    def __init__(self, positions: [tuple] = None) -> None:
        if positions:
            self.vecs = set()
            for pos in positions:
                self.vecs.add(pos)

    def read_data(self, data: [str]):
        width = len(data[0])
        height = len(data)

        vecs = set()

        for x in range(width):
            for y in range(height):
                char = data[y][x]
                if char == '#':
                    vecs.add((x, y))

        self.vecs = vecs

    def determine_visible(self, vec_to_check: tuple):
        occlusions = self.determine_occlusions(vec_to_check)
        visible = self.vecs.difference(occlusions)
        visible.remove(vec_to_check)
        return visible

    def determine_occlusions(self, vec_to_check: tuple, max_occlusions: int = None):
        vecs = list(self.vecs.copy())
        vecs.remove(vec_to_check)

        occlusions = set()

        while vecs:
            v1 = vecs.pop()
            new_vecs_to_remove = set()
            for v2 in vecs:
                v1_dir = np.array(v1) - np.array(vec_to_check)
                v2_dir = np.array(v2) - np.array(vec_to_check)

                cos_dist = AsteroidScanner.cosine_distance(v1_dir, v2_dir)
                if 0 != cos_dist and 1 - cos_dist <= 0.00000000000001:
                    if norm(np.array(vec_to_check) - np.array(v1)) < norm(np.array(vec_to_check) - np.array(v2)):
                        occlusions.add(v2)
                        new_vecs_to_remove.add(v2)
                        if max_occlusions and len(occlusions) > max_occlusions:
                            print('Stopping early, max occlusions exceeded: {}'.format(len(occlusions)))
                            return occlusions
                    else:
                        occlusions.add(v1)
                        if max_occlusions and len(occlusions) > max_occlusions:
                            print('Stopping early, max occlusions exceeded: {}'.format(len(occlusions)))
                            return occlusions
                        break
            for occluded_vec in new_vecs_to_remove:
                vecs.remove(occluded_vec)

        return occlusions

    def determine_best(self):
        current_best = None
        current_most_visible = 0
        max_occlusions = sys.maxsize
        counter = 0

        for vec in self.vecs:
            occlusions = len(self.determine_occlusions(vec, max_occlusions=max_occlusions))
            if occlusions < max_occlusions:
                max_occlusions = occlusions
                current_best = vec
                current_most_visible = len(self.vecs) - max_occlusions - 1
            counter += 1
            print('Positions remaining: {}'.format(len(self.vecs) - counter))
        return current_best, current_most_visible

    def vaporize(self, station_pos: tuple):
        laser_direction = (np.array((0, -1)) + np.array(station_pos)) * np.array((1, -1))

        count = 0

        while len(self.vecs) > 1:
            visible = self.determine_visible(station_pos)
            l = list(visible)
            list_right = list()
            for v in visible:
                if v[0] >= laser_direction[0]:
                    list_right.append(v)
            list_left = list()
            for v in visible:
                if v[0] < laser_direction[0]:
                    list_left.append(v)

            list_right.sort(key=lambda a: AsteroidScanner.cosine_distance(np.array(a) - np.array(station_pos),
                                                                          laser_direction - np.array(station_pos)), reverse=True)
            list_left.sort(key=lambda a: AsteroidScanner.cosine_distance(np.array(a) - np.array(station_pos),
                                                                          laser_direction - np.array(station_pos)))
            l = list()
            l.extend(list_right)
            l.extend(list_left)
            for a in l:
                print('{} -> cos: {}'.format(a, AsteroidScanner.cosine_distance(np.array(a) - np.array(station_pos),
                                                                                laser_direction - np.array(
                                                                                    station_pos))))


            print('Laser: {}'.format(laser_direction))
            for a in l:
                count += 1
                print('The {}. asteroid to be vaporized is at {}.'.format(count, a))
                self.vecs.remove(a)

    @staticmethod
    def cosine_distance(vec1, vec2) -> float:
        return dot(vec1, vec2) / (norm(vec1) * norm(vec2))
