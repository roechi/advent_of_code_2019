from nose.tools import assert_equal

from day_6.MapNavigator import OrbitTree, Node


def test_add_and_count_direct():
    tree = OrbitTree('O')
    tree.add('O', 'A')
    tree.add('O', 'B')
    tree.add('A', 'AA')

    direct_orbits_count = tree.count_direct_orbits()
    assert_equal(direct_orbits_count, 3)

    tree.add('A', 'AAA')
    tree.add('B', 'C')

    direct_orbits_count = tree.count_direct_orbits()
    assert_equal(direct_orbits_count, 5)


def test_add_and_count_indirect():
    tree = OrbitTree('O')
    tree.add('O', 'A')
    tree.add('A', 'B')
    tree.add('A', 'C')
    tree.add('A', 'D')

    direct_orbits_count = tree.count_indirect_orbits()
    assert_equal(direct_orbits_count, 3)

    tree.add('B', 'E')
    tree.add('B', 'F')

    direct_orbits_count = tree.count_indirect_orbits()
    assert_equal(direct_orbits_count, 7)


def test_for_given_map():
    tree = OrbitTree('COM')
    tree.add('COM', 'B')
    tree.add('B', 'G')
    tree.add('G', 'H')
    tree.add('B', 'C')
    tree.add('C', 'D')
    tree.add('D', 'I')
    tree.add('D', 'E')
    tree.add('E', 'J')
    tree.add('J', 'K')
    tree.add('K', 'L')
    tree.add('E', 'F')

    total_orbits = tree.count_direct_orbits() + tree.count_indirect_orbits()
    assert_equal(total_orbits, 42)


def test_LCA_for_given_map():
    tree = OrbitTree('COM')
    tree.add('COM', 'B')
    tree.add('B', 'G')
    tree.add('G', 'H')
    tree.add('B', 'C')
    tree.add('C', 'D')
    tree.add('D', 'I')
    tree.add('D', 'E')
    tree.add('E', 'J')
    tree.add('J', 'K')
    tree.add('K', 'L')
    tree.add('E', 'F')
    tree.add('K', 'US')
    tree.add('I', 'SAN')

    lca = tree.find_LCA('US', 'SAN')
    assert_equal(lca.data, 'D')


def test_find_path_for_given_map():
    tree = OrbitTree('COM')
    tree.add('COM', 'B')
    tree.add('B', 'G')
    tree.add('G', 'H')
    tree.add('B', 'C')
    tree.add('C', 'D')
    tree.add('D', 'I')
    tree.add('D', 'E')
    tree.add('E', 'J')
    tree.add('J', 'K')
    tree.add('K', 'L')
    tree.add('E', 'F')
    tree.add('K', 'US')
    tree.add('I', 'SAN')

    path = tree.find_path('US')
    assert_equal(path, 6)


def test_find_path_between_for_given_map():
    tree = OrbitTree('COM')
    tree.add('COM', 'B')
    tree.add('B', 'G')
    tree.add('G', 'H')
    tree.add('B', 'C')
    tree.add('C', 'D')
    tree.add('D', 'I')
    tree.add('D', 'E')
    tree.add('E', 'J')
    tree.add('J', 'K')
    tree.add('K', 'L')
    tree.add('E', 'F')
    tree.add('K', 'US')
    tree.add('I', 'SAN')

    path = tree.find_shortest_path_between('US', 'SAN')
    assert_equal(path, 4)


def test_result_part_one():
    t = open('../resources/input_6.txt')
    lines = t.readlines()
    t.close()

    orbit_tupels = list(map(split_to_orbit_tuple, lines))

    tree = OrbitTree('COM')
    build_tree(tree, 'COM', orbit_tupels)

    orbits = tree.count_direct_orbits() + tree.count_indirect_orbits()
    print('The total number of orbits is: ' + str(orbits))


def test_result_part_two():
    t = open('../resources/input_6.txt')
    lines = t.readlines()
    t.close()

    orbit_tupels = list(map(split_to_orbit_tuple, lines))

    tree = OrbitTree('COM')
    build_tree(tree, 'COM', orbit_tupels)

    path_len = tree.find_shortest_path_between('YOU', 'SAN')
    print('The shortest path between us and Santa requires: ' + str(path_len) + ' transitions.')


def build_tree(tree: OrbitTree, id: str, tuples: [tuple]):
    next_nodes = next_to_append(id, tuples)
    for n in next_nodes:
        tree.add(n[0], n[1])
        build_tree(tree, n[1], tuples)


def next_to_append(id: str, tuples: list) -> [tuple]:
    return list(filter(lambda tup: tup[0] == id, tuples))


def split_to_orbit_tuple(line: str) -> tuple:
    obs = line.strip().split(')')
    return obs[0], obs[1]

