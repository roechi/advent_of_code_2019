from functools import reduce

import numpy as np
from math import gcd


class MoonTracker:
    def __init__(self, positions: [tuple]) -> None:
        self.bodies = list()
        self.dimensions = len(positions[0])
        for p in positions:
            self.bodies.append([np.array(p), np.array([0 for d in range(self.dimensions)])])

    def apply_step(self):
        for b in self.bodies:
            for o_b in self.bodies:
                if not (o_b[0] == b[0]).all():
                    for d in range(self.dimensions):
                        if o_b[0][d] > b[0][d]:
                            b[1][d] += 1
                        elif o_b[0][d] < b[0][d]:
                            b[1][d] -= 1

        for b in self.bodies:
            b[0] += b[1]

    def calc_system_energy(self) -> int:
        total_energy = 0
        for b in self.bodies:
            total_energy += abs(b[0]).sum() * abs(b[1]).sum()

        return total_energy

    def simulate_until_state_repeats(self) -> int:

        seen_coords = [set() for d in range(self.dimensions)]
        coords_have_repeated = [None for d in range(self.dimensions)]

        step = 0

        while not all(v is not None for v in coords_have_repeated):
            for d in range(self.dimensions):
                if not coords_have_repeated[d]:
                    d_state = list()
                    for b in self.bodies:
                        d_state.append(b[0][d])
                        d_state.append(b[1][d])
                    if str(d_state) in seen_coords[d]:
                        print('Found dim {}: {}'.format(d, step))
                        coords_have_repeated[d] = step
                    seen_coords[d].add(str(d_state))

            self.apply_step()
            step += 1

        return reduce(lambda step1, step2: MoonTracker.lcm(step1, step2), coords_have_repeated)

    @staticmethod
    def lcm(x, y):
        return x // gcd(x, y) * y
