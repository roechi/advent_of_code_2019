from functools import reduce

from day_13.IntcodeComputer import IntcodeComputer
import sys

class TractorBeam:
    def __init__(self) -> None:
        t = open('../resources/input_19.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))
        self.computer = IntcodeComputer(program)

    def get_affected_fields(self, max_x: int, max_y: int):
        affected = 0
        for x in range(max_x):
            for y in range(max_y):
                mem, out, exit_code = self.computer.run_program(input=[x, y])
                if out:
                    if out[0] == 1:
                        affected += 1
                        print('{}, {} -> {}'.format(x, y, out))

        return affected

    def fit_ship(self):
        x = 0
        y = 0
        affected_area = set()
        left_edge = 0
        for y in range(1000):
            found_in_line = False
            for x in range(left_edge, 1000):
                mem, out, exit_code = self.computer.run_program(input=[x, y])
                if out:
                    if out[0] == 1:
                        if not found_in_line:
                            found_in_line = True
                            left_edge = x
                        affected_area.add((x, y))
                    elif out[0] == 0:
                        if found_in_line:
                            break
                if len(affected_area) >= 100 * 100:
                    for pos in affected_area:
                        xx = pos[0]
                        yy = pos[1]
                        if (xx + 99, yy) in affected_area and (xx, yy + 99) in affected_area and (
                        xx + 99, yy + 99) in affected_area:
                            return (xx, yy)

    def fit_better(self):
        left_edge = 0
        y = 0
        affected_area = list()
        while True:
            found_in_line = False
            for x in range(left_edge, left_edge + 100):
                mem, out, exit_code = self.computer.run_program(input=[x, y])
                if out[0] == 1:
                    if not found_in_line:
                        found_in_line = True
                        left_edge = x
                        for xx in range(left_edge, left_edge + 100):

                            mem, out, exit_code = self.computer.run_program(input=[xx, y])
                            if out[0] == 1:
                                affected_area.append((xx, y))
                                if (xx - 100, y - 100) in affected_area:
                                    if (xx - 100, y) in affected_area and (xx, y -100) in affected_area:
                                        return (xx - 100, y - 100)
                            elif out[0] == 0:
                                if found_in_line:
                                    #TractorBeam.print_beam(x, xx, True)
                                    break
                    break
            #if not found_in_line:
             #   TractorBeam.print_beam(left_edge, left_edge + 100, False)
            y += 1

    def fit_even_better(self):
        s_length = 99
        x = 0
        y = 100
        while True:
            while True:
                mem, out, exit_code = self.computer.run_program(input=[x, y])
                if out[0] == 1:
                    if self.computer.run_program(input=[x + s_length, y - s_length])[1][0] == 1:
                        return x * 10000 + y - 99
                    else:
                        break
                else:
                    x += 1
            y += 1
            #13690873 wrong


    @staticmethod
    def print_beam(le, re, found):
        s = reduce(lambda l,r: l + r, ['.' for x in range(le)], '.')
        if found:
            s += reduce(lambda l, r: l + r, ['#' for x in range(le, re)], '.')
        else:
            s += reduce(lambda l, r: l + r, ['.' for x in range(le, re)], '.')
        print(s)
