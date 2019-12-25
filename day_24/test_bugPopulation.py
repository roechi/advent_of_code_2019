from unittest import TestCase

from nose.tools import assert_equal

from day_24.BugPopulation import BugPopulation


class TestBugPopulation(TestCase):
    def test___init__(self):
        raw = ['....#\n',
               '#..#.\n',
               '#..##\n',
               '..#..\n',
               '#....']

        bp = BugPopulation(raw)

        bd_rating = bp.cycle_until_duplicate()

        assert_equal(bd_rating, 2129920)

    def test___init__2(self):
        raw = ['....#\n',
               '#..#.\n',
               '#..##\n',
               '..#..\n',
               '#....']

        bp = BugPopulation(raw)

        for i in range(10):
            bp.cycle()

        bug_count = bp.get_total_bug_count()
        assert_equal(bug_count, 99)

    def test_solve_2(self):
        t = open('../resources/input_24.txt')
        raw = t.readlines()
        t.close()

        bp = BugPopulation(raw)

        for i in range(200):
            bp.cycle()

        bug_count = bp.get_total_bug_count()
        print(bug_count)

