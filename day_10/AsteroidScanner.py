import numpy as np
from numpy.linalg import norm
from numpy import dot


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

    def determine_occlusions(self, vec_to_check: tuple):
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
                    else:
                        occlusions.add(v1)
                        break
            for occluded_vec in new_vecs_to_remove:
                vecs.remove(occluded_vec)

        return occlusions

    def determine_best(self):
        current_best = None
        current_most_visible = 0

        counter = 0

        for vec in self.vecs:
            visible = self.determine_visible(vec)
            if len(visible) > current_most_visible:
                current_most_visible = len(visible)
                current_best = vec
            counter += 1
            print('Positions to remaining: {}'.format(len(self.vecs) - counter))
        return current_best, current_most_visible

    @staticmethod
    def cosine_distance(vec1, vec2) -> float:
        return dot(vec1, vec2) / (norm(vec1) * norm(vec2))
