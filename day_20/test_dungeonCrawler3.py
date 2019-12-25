from unittest import TestCase

from nose.tools import assert_equal

from day_20.DungeonCrawler3 import DungeonCrawler3


class TestDungeonCrawler3(TestCase):
    def test_dijkstra_1(self):
        map_str = ['         A           \n',
                   '         A           \n',
                   '  #######.#########  \n',
                   '  #######.........#  \n',
                   '  #######.#######.#  \n',
                   '  #######.#######.#  \n',
                   '  #######.#######.#  \n',
                   '  #####  B    ###.#  \n',
                   'BC...##  C    ###.#  \n',
                   '  ##.##       ###.#  \n',
                   '  ##...DE  F  ###.#  \n',
                   '  #####    G  ###.#  \n',
                   '  #########.#####.#  \n',
                   'DE..#######...###.#  \n',
                   '  #.#########.###.#  \n',
                   'FG..#########.....#  \n',
                   '  ###########.#####  \n',
                   '             Z       \n',
                   '             Z       \n']

        dc = DungeonCrawler3(map_str)
        start = None
        end = None

        for p in dc.portals.keys():
            if dc.portals[p] == 'AA':
                start = p
            elif dc.portals[p] == 'ZZ':
                end = p

        dist = dc.dijkstra(start, end)
        print(dist)
        assert_equal(dist, 23)

    def test_dijkstra_2(self):
        map_str = ['                   A               \n',
                   '                   A               \n',
                   '  #################.#############  \n',
                   '  #.#...#...................#.#.#  \n',
                   '  #.#.#.###.###.###.#########.#.#  \n',
                   '  #.#.#.......#...#.....#.#.#...#  \n',
                   '  #.#########.###.#####.#.#.###.#  \n',
                   '  #.............#.#.....#.......#  \n',
                   '  ###.###########.###.#####.#.#.#  \n',
                   '  #.....#        A   C    #.#.#.#  \n',
                   '  #######        S   P    #####.#  \n',
                   '  #.#...#                 #......VT\n',
                   '  #.#.#.#                 #.#####  \n',
                   '  #...#.#               YN....#.#  \n',
                   '  #.###.#                 #####.#  \n',
                   'DI....#.#                 #.....#  \n',
                   '  #####.#                 #.###.#  \n',
                   'ZZ......#               QG....#..AS\n',
                   '  ###.###                 #######  \n',
                   'JO..#.#.#                 #.....#  \n',
                   '  #.#.#.#                 ###.#.#  \n',
                   '  #...#..DI             BU....#..LF\n',
                   '  #####.#                 #.#####  \n',
                   'YN......#               VT..#....QG\n',
                   '  #.###.#                 #.###.#  \n',
                   '  #.#...#                 #.....#  \n',
                   '  ###.###    J L     J    #.#.###  \n',
                   '  #.....#    O F     P    #.#...#  \n',
                   '  #.###.#####.#.#####.#####.###.#  \n',
                   '  #...#.#.#...#.....#.....#.#...#  \n',
                   '  #.#####.###.###.#.#.#########.#  \n',
                   '  #...#.#.....#...#.#.#.#.....#.#  \n',
                   '  #.###.#####.###.###.#.#.#######  \n',
                   '  #.#.........#...#.............#  \n',
                   '  #########.###.###.#############  \n',
                   '           B   J   C               \n',
                   '           U   P   P               \n']

        dc = DungeonCrawler3(map_str)
        start = None
        end = None

        for p in dc.portals.keys():
            if dc.portals[p] == 'AA':
                start = p
            elif dc.portals[p] == 'ZZ':
                end = p

        dist = dc.dijkstra(start, end)
        print(dist)
        assert_equal(dist, 58)

    def test_dijkstra_3_folded(self):
        map_str = ['             Z L X W       C                 \n',
                   '             Z P Q B       K                 \n',
                   '  ###########.#.#.#.#######.###############  \n',
                   '  #...#.......#.#.......#.#.......#.#.#...#  \n',
                   '  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  \n',
                   '  #.#...#.#.#...#.#.#...#...#...#.#.......#  \n',
                   '  #.###.#######.###.###.#.###.###.#.#######  \n',
                   '  #...#.......#.#...#...#.............#...#  \n',
                   '  #.#########.#######.#.#######.#######.###  \n',
                   '  #...#.#    F       R I       Z    #.#.#.#  \n',
                   '  #.###.#    D       E C       H    #.#.#.#  \n',
                   '  #.#...#                           #...#.#  \n',
                   '  #.###.#                           #.###.#  \n',
                   '  #.#....OA                       WB..#.#..ZH\n',
                   '  #.###.#                           #.#.#.#  \n',
                   'CJ......#                           #.....#  \n',
                   '  #######                           #######  \n',
                   '  #.#....CK                         #......IC\n',
                   '  #.###.#                           #.###.#  \n',
                   '  #.....#                           #...#.#  \n',
                   '  ###.###                           #.#.#.#  \n',
                   'XF....#.#                         RF..#.#.#  \n',
                   '  #####.#                           #######  \n',
                   '  #......CJ                       NM..#...#  \n',
                   '  ###.#.#                           #.###.#  \n',
                   'RE....#.#                           #......RF\n',
                   '  ###.###        X   X       L      #.#.#.#  \n',
                   '  #.....#        F   Q       P      #.#.#.#  \n',
                   '  ###.###########.###.#######.#########.###  \n',
                   '  #.....#...#.....#.......#...#.....#.#...#  \n',
                   '  #####.#.###.#######.#######.###.###.#.#.#  \n',
                   '  #.......#.......#.#.#.#.#...#...#...#.#.#  \n',
                   '  #####.###.#####.#.#.#.#.###.###.#.###.###  \n',
                   '  #.......#.....#.#...#...............#...#  \n',
                   '  #############.#.#.###.###################  \n',
                   '               A O F   N                     \n',
                   '               A A D   M                     \n']

        dc = DungeonCrawler3(map_str, folded=True)
        start = None
        end = None

        for p in dc.portals.keys():
            if dc.portals[p] == 'AA':
                start = p
            elif dc.portals[p] == 'ZZ':
                end = p

        dist = dc.dijkstra(start, end)
        print(dist)
        assert_equal(dist, 396)

    def test_solve_part_1(self):
        t = open('../resources/input_20_mod.txt')
        l = t.readlines()
        t.close()

        dc = DungeonCrawler3(l)
        start = None
        end = None

        for p in dc.portals.keys():
            if dc.portals[p] == 'AA':
                start = p
            elif dc.portals[p] == 'ZZ':
                end = p

        dist = dc.dijkstra(start, end)
        assert_equal(dist, 602)

    def test_solve_part_2(self):
        t = open('../resources/input_20_mod.txt')
        l = t.readlines()
        t.close()

        dc = DungeonCrawler3(l, folded=True)
        start = None
        end = None

        for p in dc.portals.keys():
            if dc.portals[p] == 'AA':
                start = p
            elif dc.portals[p] == 'ZZ':
                end = p

        dist = dc.dijkstra(start, end)
        assert_equal(dist, 6986)

