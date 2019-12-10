from unittest import TestCase
import numpy as np
from nose.tools import assert_equal

from day_10.AsteroidScanner import AsteroidScanner


class TestAsteroidScanner(TestCase):
    def test_determine_occlusions(self):
        scanner = AsteroidScanner([(0, 0), (1, 1), (2, 2), (0, 1)])

        occlusions = scanner.determine_occlusions((0, 0))

        assert_equal(len(occlusions), 1)
        assert_equal(occlusions.pop(), (2, 2))

    def test_read_asteroid_data_1(self):
        data = ['.#..#',
                '.....',
                '#####',
                '....#',
                '...##']

        scanner = AsteroidScanner()
        scanner.read_data(data)
        expected = {(1, 2), (3, 2), (4, 4), (4, 3), (2, 2), (4, 2), (1, 0), (3, 4), (0, 2), (4, 0)}
        assert_equal(expected, scanner.vecs)

        visible = scanner.determine_visible((4, 2))
        assert_equal(len(visible), 5)

        visible = scanner.determine_visible((1, 0))
        assert_equal(len(visible), 7)

        visible = scanner.determine_visible((4, 4))
        assert_equal(len(visible), 7)

        visible = scanner.determine_visible((3, 4))
        assert_equal(len(visible), 8)


    def test_read_asteroid_data_2(self):
        data = ['......#.#.',
                '#..#.#....',
                '..#######.',
                '.#.#.###..',
                '.#..#.....',
                '..#....#.#',
                '#..#....#.',
                '.##.#..###',
                '##...#..#.',
                '.#....####']

        scanner = AsteroidScanner()
        scanner.read_data(data)

        visible = scanner.determine_visible((5, 8))
        assert_equal(len(visible), 33)

    def test_read_asteroid_data_3(self):
        data = ['#.#...#.#.',
                '.###....#.',
                '.#....#...',
                '##.#.#.#.#',
                '....#.#.#.',
                '.##..###.#',
                '..#...##..',
                '..##....##',
                '......#...',
                '.####.###.',]

        scanner = AsteroidScanner()
        scanner.read_data(data)

        best_vec, visible = scanner.determine_best()

        assert_equal(best_vec, (1, 2))
        assert_equal(visible, 35)

    def test_result_part_one(self):
        t = open('../resources/input_10.txt')
        lines = t.readlines()
        t.close()

        lines = list(map(str.strip, lines))

        scanner = AsteroidScanner()
        scanner.read_data(lines)

        best_vec, visible = scanner.determine_best()
        print('The best possible position is {} with {} visible asteroids.'.format(best_vec, visible))
