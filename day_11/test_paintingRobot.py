from unittest import TestCase
import numpy as np

from day_11.PaintingRobot import PaintingRobot


class TestPaintingRobot(TestCase):

    def test_result_part_one_day_eleven(self):
        t = open('../resources/input_11.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))
        robot = PaintingRobot(program)

        painted_at_least_once = robot.paint()
        print('Painted at least once: {}'.format(len(painted_at_least_once)))

    def test_result_part_two_day_eleven(self):
        t = open('../resources/input_11.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))
        robot = PaintingRobot(program, {(0, 0) : 1})

        painted_at_least_once = robot.paint()

        panels = robot.visited_panels

        image = [[0 for i in range(10)] for j in range(50)]

        for p in panels.keys():
            image[p[0]][p[1]] = panels[p]

        n_image = np.array(image).transpose()

        print(n_image.transpose())
        # -> 'HAFULAPE'
