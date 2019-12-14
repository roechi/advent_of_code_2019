from nose.tools import assert_equal

from day_14.NanoFactory import NanoFactory

ONE_TRILLION = 1000000000000


def test_nano_factory():
    inputs = ['10 ORE => 10 A',
              '1 ORE => 1 B',
              '7 A, 1 B => 1 C',
              '7 A, 1 C => 1 D',
              '7 A, 1 D => 1 E',
              '7 A, 1 E => 1 FUEL']

    factory = NanoFactory(inputs)
    ore = factory.solve()
    assert_equal(len(factory.reaction_table), 6)
    assert_equal(ore, 31)


def test_nano_factory_3():
    inputs = ['157 ORE => 5 NZVS',
              '165 ORE => 6 DCFZ',
              '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
              '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
              '179 ORE => 7 PSHF',
              '177 ORE => 5 HKGWZ',
              '7 DCFZ, 7 PSHF => 2 XJWVT',
              '165 ORE => 2 GPVTF',
              '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']

    factory = NanoFactory(inputs)
    ore = factory.solve()
    assert_equal(len(factory.reaction_table), 9)
    assert_equal(ore, 13312)
    max_fuel = factory.produce_fuel(ONE_TRILLION)
    assert_equal(max_fuel, 82892753)


def test_nano_factory_2():
    inputs = [
        '9 ORE => 2 A',
        '8 ORE => 3 B',
        '7 ORE => 5 C',
        '3 A, 4 B => 1 AB',
        '5 B, 7 C => 1 BC',
        '4 C, 1 A => 1 CA',
        '2 AB, 3 BC, 4 CA => 1 FUEL']

    factory = NanoFactory(inputs)
    ore = factory.solve()
    assert_equal(len(factory.reaction_table), 7)
    assert_equal(ore, 165)


def test_result_part_one():
    t = open('../resources/input_14.txt')
    lines = t.readlines()
    lines = list(map(lambda l: l.rstrip("\n\r"), lines))
    t.close()

    factory = NanoFactory(lines)
    ore = factory.solve()
    print('Required ore: {}'.format(ore))
    assert_equal(ore, 502491)

    max_fuel = factory.produce_fuel(ONE_TRILLION)
    print('Max fuel: {}'.format(max_fuel))
