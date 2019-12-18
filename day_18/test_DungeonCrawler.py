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

    dist, tree = dc.dijkstra(dc.map, (1, 1), (5, 1), ['d', 'e'])
    assert_equal(dist, 4)

    min_path_len = dc.solve()

    assert_equal(min_path_len, 86)


def test_solve_3():
    map_str = ['########################\n',
               '#...............b.C.D.f#\n',
               '#.######################\n',
               '#.....@.a.B.c.d.A.e.F.g#\n',
               '########################\n']

    dc = DungeonCrawler(map_str)

    min_path_len = dc.solve()

    assert_equal(min_path_len, 132)


def test_solve_4():
    map_str = ['#################\n',
               '#i.G..c...e..H.p#\n',
               '########.########\n',
               '#j.A..b...f..D.o#\n',
               '########@########\n',
               '#k.E..a...g..B.n#\n',
               '########.########\n',
               '#l.F..d...h..C.m#\n',
               '#################\n']

    dc = DungeonCrawler(map_str)

    min_path_len = dc.solve()

    assert_equal(min_path_len, 136)
