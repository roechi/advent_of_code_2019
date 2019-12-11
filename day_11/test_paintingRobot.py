from unittest import TestCase

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
