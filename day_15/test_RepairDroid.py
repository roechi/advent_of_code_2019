from unittest import TestCase

from nose.tools import assert_equal

from day_15.RepairDroid import RepairDroid


class TestRun_program(TestCase):
    def test_solve(self):
        t = open('../resources/input_15.txt')
        lines = t.readlines()
        t.close()
        program = list(map(lambda x: int(x), lines[0].split(sep=',')))
        droid = RepairDroid(program)

        path, oxy_pos = droid.find()

        print('Path: {}'.format(path))
        print('Steps: {}'.format(len(path)))

        assert_equal(len(path), 218)

        minutes_for_oxygenation = droid.oxygenate(oxy_pos)
        print('It takes {} minutes to oxygenate the section.'.format(minutes_for_oxygenation))
