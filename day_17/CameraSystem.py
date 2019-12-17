from functools import reduce
import numpy as np

from day_13.IntcodeComputer import IntcodeComputer


class CameraSystem:
    def __init__(self, ) -> None:
        t = open('../resources/input_17.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))
        self.computer = IntcodeComputer(program)
        self.image = ''
        self.intersections = list()

    def show_image(self):
        mem, out, exit_code = self.computer.run_program(reset_memory=False, reset_pointer=False,
                                                        reset_relative_pointer=False)

        s = reduce(lambda x, y: x + y, map(lambda x: str(chr(x)), out))
        self.image = s
        print(s)

    def find_intersections(self):
        img = self.image
        length = self.image.index('\n') + 1
        height = int(len(self.image) / length)
        intersections = list()

        for y in range(height):
            for x in range(length):
                if 0 < y < height - 1 and 0 < x < length - 1:
                    if (img[x - 1 + y * length] == '#' and img[x + y * length] == '#' and img[x + 1 + y * length] == '#'
                            and img[x + (y - 1) * length] == '#' and img[x + (y + 1) * length] == '#'):
                        img = img[:x + y * length] + 'O' + img[x + 1 + y * length:]
                        intersections.append((x, y))

        print(img)
        self.intersections = intersections
        print('Sum of alignment params: {}'.format(np.array(list(map(lambda t: t[0] * t[1], intersections))).sum()))

    def rescue(self):
        mem, out, exit_code = self.computer.run_program(parameters=[2])

        s = reduce(lambda x, y: x + y, map(lambda x: str(chr(x)), out))

        main = list(map(lambda c: ord(c), 'A,B,C,B,A,C\n'))

        mem, out, exit_code = self.computer.run_program(input=main, reset_memory=False, reset_pointer=False,
                                                        reset_relative_pointer=False)

        s = reduce(lambda x, y: x + y, map(lambda x: str(chr(x)), out))
        A = 'L,4,L,6\n'
        C = 'R,8\n'


