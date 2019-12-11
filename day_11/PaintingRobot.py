from day_9.IntcodeComputer import IntcodeComputer
import numpy as np
from numpy import dot

class PaintingRobot:
    def __init__(self, program: [int]) -> None:
        self.computer = IntcodeComputer(program)
        self.position = (0, 0)
        self.visited_panels = dict()
        self.direction = (0, -1)

        rot_left = np.array([0, -1, 1, 0])
        rot_left = rot_left.reshape([2, 2])
        self.rot_left = rot_left

        rot_right = np.array([0, 1, -1, 0])
        rot_right = rot_right.reshape([2, 2])
        self.rot_right = rot_right

    def paint(self):

        ex_code = 1

        while ex_code != 0:
            if self.position in self.visited_panels:
                current_panel_color = self.visited_panels[self.position]
            else:
                current_panel_color = 0

            mem, out, ex_code = self.computer.run_program(input=[current_panel_color],
                                  reset_memory=False,
                                  reset_pointer=False,
                                  reset_relative_pointer=False)

            color_to_paint = out[0]
            self.visited_panels[self.position] = color_to_paint

            rotation = out[1]
            n_direction = np.array(self.direction)
            if rotation == 0:
                n_direction = np.array(self.direction).dot(self.rot_left)
            elif rotation == 1:
                n_direction = np.array(self.direction).dot(self.rot_right)

            self.direction = (n_direction[0], n_direction[1])
            n_position = np.array(self.position) + n_direction
            self.position = (n_position[0], n_position[1])

        return set(self.visited_panels.keys())




