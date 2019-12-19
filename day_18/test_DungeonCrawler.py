from nose.tools import assert_equal

from day_18.DungeonCrawler2 import DungeonCrawler2


def test_parse_map_str():
    map_str = ['#########\n',
               '#b.A.@.a#\n',
               '#########\n']

    dc = DungeonCrawler2(map_str)


def test_solve():
    map_str = ['#########\n',
               '#b.A.@.a#\n',
               '#########\n']

    dc = DungeonCrawler2(map_str)
    min_path_len = dc.solve()

    assert_equal(min_path_len, 8)


def test_solve_2():
    map_str = ['########################\n',
               '#f.D.E.e.C.b.A.@.a.B.c.#\n',
               '######################.#\n',
               '#d.....................#\n',
               '########################\n']

    dc = DungeonCrawler2(map_str)
    min_path_len = dc.solve()
    assert_equal(min_path_len, 86)


def test_solve_3():
    map_str = ['########################\n',
               '#...............b.C.D.f#\n',
               '#.######################\n',
               '#.....@.a.B.c.d.A.e.F.g#\n',
               '########################\n']

    dc = DungeonCrawler2(map_str)

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

    dc = DungeonCrawler2(map_str)

    min_path_len = dc.solve()

    assert_equal(min_path_len, 136)

def test_solve_part_1():
    t = open('../resources/input_18.txt')
    l = t.readlines()
    t.close()

    dc = DungeonCrawler2(l)

    min_path_len = dc.solve()

    assert_equal(min_path_len, 3586)

def test_solve_part_2():
    t = open('../resources/input_18_2.txt')
    l = t.readlines()
    t.close()

    dc = DungeonCrawler2(l)

    min_path_len = dc.solve()

    assert_equal(min_path_len, 1974)
