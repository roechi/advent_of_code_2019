from collections import deque
from functools import reduce
import numpy as np

class FrequencyStabilizer:
    def __init__(self, freq: [int]) -> None:
        self.freq = freq
        self.base = [0, 1, 0, -1]

    def apply_phase(self, times: int = 1):
        for t in range(times):
            print('Step {}'.format(t))
            phased = list()
            for i in range(len(self.freq)):
                pattern = FrequencyStabilizer.adjust_pattern(self.base, i)
                pattern.rotate(-1)

                result = 0
                for x in range(len(self.freq)):
                    result += self.freq[x] * pattern[0]
                    pattern.rotate(-1)
                phased.append(abs(result) % 10)
            self.freq = np.array(phased)
        return self.freq


    @staticmethod
    def adjust_pattern(pattern: [int], reps: int):
        adjusted = deque([p for p in pattern for _ in range(reps + 1)])
        return adjusted

    @staticmethod
    def shift(vec: [int], offset: int = 1):
        shifted = [0 for i in range(offset)]
        shifted.extend(vec)

        return shifted[:len(vec)]
