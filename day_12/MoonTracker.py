import numpy as np


class MoonTracker:
    def __init__(self, positions: [tuple]) -> None:
        self.bodies = list()
        for p in positions:
            self.bodies.append([np.array(p), np.array((0, 0, 0))])

        #for b in self.bodies:
         #   print(b)

    def apply_step(self):
        for b in self.bodies:
            for o_b in self.bodies:
                if not (o_b[0] == b[0]).all():
                    for i in range(len(b[0])):
                        if o_b[0][i] > b[0][i]:
                            b[1][i] += 1
                        elif o_b[0][i] < b[0][i]:
                            b[1][i] -= 1

        for b in self.bodies:
            b[0] += b[1]
            #print(b)

    def calc_system_energy(self) -> int:
        total_energy = 0
        for b in self.bodies:
            total_energy += abs(b[0]).sum() * abs(b[1]).sum()

        return total_energy

    def simulate_until_state_repeats(self) -> int:
        step = 0
        repeated = False

        states = list()
        state = list()
        for b in self.bodies:
            state.append(np.concatenate(b))

        states.append(tuple(np.concatenate(state)))

        while not repeated:
            step += 1
            if step % 1000 == 0:
                print('Step: {}'.format(step))
            self.apply_step()
            s = list()
            for b in self.bodies:
                s.append(np.concatenate(b))

            if tuple(np.concatenate(s)) in states:
                return step
            else:
                states.append(tuple(np.concatenate(s)))

        return step

    @staticmethod
    def states_equal(s1: [[np.array]], s2: [[np.array]]) -> bool:

        for i in range(len(s1)):
            if (s1[i][0] != s2[i][0]).any():
                return False
            if (s1[i][0] != s2[i][0]).any():
                return False

        return True
