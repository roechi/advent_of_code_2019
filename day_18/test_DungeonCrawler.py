from nose.tools import assert_equal

from day_18.DungeonCrawler import DungeonCrawler


def test_parse_map_str():
    map_str = ['#########\n',
               '#b.A.@.a#\n',
               '#########\n']

    dc = DungeonCrawler(map_str)


def test_solve():
    map_str = ['#########\n',
               '#b.A.@.a#\n',
               '#########\n']

    dc = DungeonCrawler(map_str)
    min_path_len = dc.solve()

    assert_equal(min_path_len, 8)


def test_solve_2():
    map_str = ['########################\n',
               '#f.D.E.e.C.b.A.@.a.B.c.#\n',
               '######################.#\n',
               '#d.....................#\n',
               '########################\n']

    dc = DungeonCrawler(map_str)
    min_path_len = dc.solve()

    assert_equal(min_path_len, 86)
